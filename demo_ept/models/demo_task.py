# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DemoTask(models.Model):
    _name = 'demo.task'
    _description = 'Demo Task'
    _order = 'priority desc, deadline, id'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()
    partner_id = fields.Many2one('res.partner', string='Customer')
    user_id = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user)
    deadline = fields.Date()
    priority = fields.Selection([('0', 'Normal'), ('1', 'High')], default='0')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], default='draft', required=True)
    is_overdue = fields.Boolean(compute='_compute_is_overdue')

    @api.depends('deadline', 'state')
    def _compute_is_overdue(self):
        today = fields.Date.context_today(self)
        for task in self:
            task.is_overdue = bool(task.deadline and task.deadline < today and task.state not in ('done', 'cancel'))

    def action_start(self):
        self.write({'state': 'in_progress'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancel'})

    def action_reset_draft(self):
        self.write({'state': 'draft'})
