# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class vocab_task(osv.osv):

    _name = 'vocab.task'
    _description = 'Form for updating Vocab weekly'
    _columns = {
        'quiz_id': fields.many2one('vocab.quiz', 'Related Quiz'),
        'era_id': fields.many2one('mahad.era', 'Era'),
        'student_id': fields.many2one('mahad.student', 'Name'),
        'done_aging': fields.integer(string='Done Aging'),
        'due_date': fields.date(string='Due Date'),
        'avg_score': fields.integer(string='Avg Score%'),
        'score': fields.integer(string='Score %'),
        'remark': fields.char(string='Remark'),
        'state' : fields.selection([('open', 'Open'), ('done', 'Done')], string='Status'),

    }
