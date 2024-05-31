from thrive import models, fields, _


class Statistics(models.Model):
    _name = 'modules.tracker.statistics'
    _description = 'Modules Trackers Modules Statistics'

    name = fields.Char(string=_('Category Name'), required=True)
    app_count = fields.Char(string=_('App Count'), required=True)
    app_ids = fields.One2many('ir.module.module', 'category_id', string=_('Apps'))

    """
    Initializes the statistics for each module category by counting the number of apps in each category
    and updating the 'modules.tracker.statistics' model accordingly. If a category does not have an
    existing record, a new one is created. If it does, the existing record is updated with the new app count.

    :return: True to indicate successful completion.
    """

    def init(self):
        apps = self.env['ir.module.module'].search([])
        categories = {}

        # Populate categories dictionary with category IDs as keys and a dictionary containing
        # the category name and initial app count as values.
        for app in apps:
            category_id = app.category_id.id
            category_name = app.category_id.name
            if category_id not in categories:
                categories[category_id] = {
                    'name': category_name,
                    'app_count': 1
                }
            else:
                categories[category_id]['app_count'] += 1

        # Iterate over the categories dictionary to create or update statistics records.
        for category_id, data in categories.items():
            category_name = data['name']
            app_count = data['app_count']

            # Search for an existing record for the category.
            category_record = self.env['modules.tracker.statistics'].search([('name', '=', category_name)], limit=1)

            # If record doesn't exist, create a new one
            if not category_record:
                self.env['modules.tracker.statistics'].create({
                    'name': category_name,
                    'app_count': app_count,
                })
            # If record exists, update its app count
            else:
                category_record.write({'app_count': app_count})

        return True
