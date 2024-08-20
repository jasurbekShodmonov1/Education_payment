from odoo import models, fields

class Group(models.Model):
    _name = 'course.group'
    _description = 'Group'

    name = fields.Char(string='Group Name', required=True)
    course_id = fields.Many2one('course.course', string='Course')
    teacher_id = fields.Many2one('course.teacher', string='Teacher')
    student_ids = fields.Many2many('course.student', string='Students')
