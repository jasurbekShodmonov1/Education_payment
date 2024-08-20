from odoo import models, fields

class Teacher(models.Model):
    _name = 'course.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Teacher Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
