from odoo import models, fields

class Student(models.Model):
    _name = 'course.student'
    _description = 'Student'

    name = fields.Char(string='Student Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    # group_ids = fields.Many2many('course.course', string='Courses')
