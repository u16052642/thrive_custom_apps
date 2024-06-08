# -*- coding: utf-8 -*-
###################################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#     Author:Anjhana A K(<https://www.thrivebureau.com>)
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
from random import randint


class ActivityTag(models.Model):
    """This class is used to create tags for activity"""
    _name = "activity.tag"
    _description = "Activity Tag"

    def _get_default_color(self):
        """to get colors for the tag"""
        return randint(1, 11)

    name = fields.Char('Tag Name', required=True, translate=True,
                       help="Tag name")
    color = fields.Integer('Color', default=_get_default_color,
                           help="Tag color")

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
