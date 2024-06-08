# -*- coding: utf-8 -*-
#############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Thrive Bureau Solutions(<https://www.thrivebureau.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from thrive import fields, models


class ProductProduct(models.Model):
    """Created the class for inheriting the product model """
    _inherit = 'product.product'

    rental = fields.Boolean('Rental',
                            help="Boolean field for checking the product is rental or not")
    category_id = fields.Many2one('rental.product.category',
                                  string='Rental Category',
                                  help="Adding rental product category")
    product_agreement_id = fields.Many2one('rental.product.agreement',
                                           string='Product Agreement',
                                           help="Set the product agreement")
    security_amount = fields.Monetary(string='Security Amount',
                                      help='To add the Security Amount')
