from thrive import models, fields, _


class Tailor(models.Model):
    _name = 'modules.tracker.modules'
    _description = 'Store Modules Data'

    name = fields.Char(string=_('Module Name'), required=True)
    version = fields.Char(string=_("Version"))
    created_at = fields.Date(string=_('Created At'))
    created_by = fields.Many2one('hr.employee', string=_('Created By'))
    tested_by = fields.Many2one('hr.employee', string=_('Tested By'))
    description = fields.Text(string=_('Description'))
    image = fields.Image(' ')

    module_state = fields.Selection([
        ('draft', 'Draft'),
        ('reviewed', 'Reviewed'),
        ('tested', 'Tested'),
        ('upgraded', 'Upgraded'),
    ], default="draft", required=True)

    multi_thrive_versions = fields.One2many('modules.tracker.thrive.versions', 'module_id', "Odoo Versions")

    multi_modules_dependents = fields.One2many('modules.tracker.modules.dependents', 'module_id',
                                               string=_("Modules Dependents"))
    multi_packages_dependents = fields.One2many('modules.tracker.python.packages.dependents', 'package_id',
                                                string=_("Python Packages "
                                                         "Dependents"))
    GH_link = fields.Char(string=_("Github Link"))
    thrive_store_link = fields.Char(string=_("Odoo Store Link"))


class OdooVersions(models.Model):
    _name = 'modules.tracker.thrive.versions'
    _description = 'Store Odoo Versions'
    _rec_name = 'thrive_version'

    thrive_version = fields.Char(string=_('Odoo Version'), required=True)
    module_id = fields.Many2one('modules.tracker.modules', string='Module')


class ModulesDependents(models.Model):
    _name = 'modules.tracker.modules.dependents'
    _description = 'Store Modules Dependents'

    module_id = fields.Many2one('modules.tracker.modules', string='Module', hide=True)
    module_name = fields.Char(string=_('Name'), required=True)
    module_version = fields.Char(string=_('Version'))


class PythonPackagesDependents(models.Model):
    _name = 'modules.tracker.python.packages.dependents'
    _description = 'Store python Packages Dependents'

    package_id = fields.Many2one('modules.tracker.modules', string='Module', hide=True)
    package_name = fields.Char(string=_('Name'), required=True)
    package_version = fields.Char(string=_('Version'))
