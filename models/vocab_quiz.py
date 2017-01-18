# -*- coding: utf-8 -*-

from openerp import api
from openerp import models, fields
from openerp.osv import fields as Fields


class vocab_quiz(models.Model):
    _name = 'vocab.quiz'
    _description = 'Quiz to create'

    def today(self):
        return fields.Date.today()

    name=fields.Char(string='ID')
    average_score = fields.Integer(string='Average Score %', compute='_compute_average_score')
    total_question = fields.Integer(string='Total Questions', compute='_compute_total_question', store=True)
    published_date=fields.Date(string='Published Date' , default=today, required='true')
    due_date=fields.Date(string='Due Date', required='true')

    line_ids=fields.One2many('vocab.quiz.line', 'quiz_id', 'Material Covered')
    task_ids=fields.One2many('vocab.task', 'quiz_id', 'Assigned Students')

    @api.one
    @api.depends('line_ids')
    def _compute_total_question(self):
        total_question = 0
        for line_id in self.line_ids:
            total_question=total_question + line_id.frequency
        self.total_question = total_question

    @api.one
    @api.depends('task_ids')
    def _compute_average_score(self):
        total_score = 0
        person = 0
        for task_id in self.task_ids:
            person=person+1
            total_score=total_score + task_id.top_score
        if person == 0:
            self.average_score = 0
        else:
            self.average_score = total_score/person





class vocab_quiz_line(models.Model):
    _name = 'vocab.quiz.line'
    _description = 'Quiz to create'

    week_id = fields.Many2one('vocab.week', 'Week Covered')
    day = fields.Integer(string='Day')
    frequency = fields.Integer(string='Frequency')
    quiz_id = fields.Many2one('vocab.quiz', 'Quiz ID')
