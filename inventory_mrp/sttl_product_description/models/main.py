# -*- coding: utf-8 -*-
################################################################################
# 
#    Generate product description based on product name
#
#    Silver Touch Technologies Limited (https://www.silvertouch.com/)
#
################################################################################

from thrive import fields, models, api
import json
import requests
import random
from datetime import datetime, timedelta
from thrive.exceptions import ValidationError

# Inheriting 'res.config.settings' and adding new field in it.
class InheritConfiguration(models.TransientModel):
    _inherit = "res.config.settings"
    
    productDescription = fields.Boolean(string="Generate Product Description",
     config_parameter="sttl_product_description.productDescription")

    # Changing value of scheduled actions for product description based on our configuration field.
    @api.onchange('productDescription')
    def toggle_product_description(self):
        param_value = self.env['ir.config_parameter'].get_param('sttl_product_description.productDescription')
        cron_id = self.env['ir.cron'].search([('cron_name', 'ilike', 'Add Product Description'),
         ('active', '=', not param_value)])
        cron_id.active = param_value
        if param_value:
            cron_id.nextcall = datetime.now() + timedelta(minutes=5)

       

class ProductDescription(models.Model):
    _inherit = "product.template"
    __description = "Generate product description for product based on name"

    # Creating method to generate product description 
    def generate_description(self):
        # Creating list of multiple prompts to get different descriptions.
        prompts = ["Create an description for product ", "Write an description for product ",
        "suggest an description for ", "Generate description for given product ",
        "Craft a detailed description for a ", "Create an enticing product narrative for a ", 
        "Develop a persuasive description for a", "Write an engaging overview for an ",
        "Develop a comprehensive description for a "]

        # Making an api request using requests module.
        API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
        API_TOKEN = "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"
        headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            'Content-Type' : 'application/json' 
        }
        desc = f"{random.choice(prompts)} {self.name}"
        query = {
            "inputs": desc,
            "options": {"wait_for_model": True},
            "parameters": {
                "max_new_tokens": 100,
                "use_cache" : False
            }
        }
        data = json.dumps(query)
        try:
            response = requests.request(
                "POST", API_URL, headers=headers, data=data)
            # Loading and and converting response data into appropriate format.
            description = json.loads(response.content.decode("utf-8"))[0]["generated_text"]
            da = description.split("\n")
            da.pop(0)
            description = "".join(da)
            da = description.split(".")
            da.pop()
            description = ".".join(da)
            description += "."
            self.description = description
            self.description_sale = description
        except:
            raise ValidationError("Unable to get product description")
    
    def generate_mass_description(self):
        product = self.env['product.template'].search(['|',('description', 'ilike', "<p><br></p>"),
         ('description', '=', False)], limit=1)
        if product:
            prompts = ["Create an description for product ", "Write an description for product ",
            "suggest an description for ", "Generate description for given product ",
            "Craft a detailed description for a ", "Create an enticing product narrative for a ", 
            "Develop a persuasive description for a", "Write an engaging overview for an ",
            "Develop a comprehensive description for a "]
            API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
            API_TOKEN = "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"
            headers = {
                "Authorization": f"Bearer {API_TOKEN}",
                'Content-Type' : 'application/json' 
            }
            try:          
                desc = f"{random.choice(prompts)} {product.name}"
                query = {
                    "inputs": desc,
                    "options": {"wait_for_model": True},
                    "parameters": {
                        "max_new_tokens": 100,
                        "use_cache" : False
                    }
                }
                data = json.dumps(query)

                response = requests.request(
                    "POST", API_URL, headers=headers, data=data)

                description = json.loads(response.content.decode("utf-8"))[0]["generated_text"]
                da = description.split("\n")
                da.pop(0)
                description = "".join(da)
                da = description.split(".")
                da.pop()
                description = ".".join(da)
                description += "."
                product.description = description
                product.description_sale = description
            except:
                raise ValidationError("Unable to get product description")
