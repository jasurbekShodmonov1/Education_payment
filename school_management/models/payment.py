from odoo import models, fields

class Payment(models.Model):
    _name = 'course.payment'
    _description = 'Payment'

    student_id = fields.Many2one('course.student', string='Student')
    amount = fields.Float(string='Amount', required=True)
    payment_date = fields.Date(string='Payment Date', default=fields.Date.today)
    description = fields.Text(string='Description')
