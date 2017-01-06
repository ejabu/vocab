# -*- coding: utf-8 -*-

from openerp.osv import fields, osv


class vocab_quiz(osv.osv):
    _name = 'vocab.quiz'
    _description = 'Quiz to create'
    _columns = {
        'name': fields.char(string='ID'),
        'average_score': fields.char(string='Average Score'),
        'total_question': fields.char(string='Total Question'),
        'published_date': fields.date(string='Published Date'),
        'due_date': fields.date(string='Due Date'),
        'line_ids': fields.one2many('vocab.quiz.line', 'quiz_id', 'Material Covered'),


    }

class vocab_quiz_line(osv.osv):
    _name = 'vocab.quiz.line'
    _description = 'Quiz to create'
    _columns = {
        'week_id': fields.many2one('vocab.week', 'Week Covered'),
        'day': fields.integer(string='Day'),
        'frequency': fields.integer(string='Frequency'),
        'quiz_id': fields.many2one('vocab.quiz', 'Quiz Id'),
    }
