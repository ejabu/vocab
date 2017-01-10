# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp import api

class vocab_task(osv.osv):

    _name = 'vocab.task'
    _inherit = ['mail.thread']
    _description = 'Assigned Task for Student'
    _columns = {
        'quiz_id': fields.many2one('vocab.quiz', 'Related Quiz'),
        'era_id': fields.many2one('mahad.era', 'Era'),
        'student_id': fields.many2one('mahad.student', 'Name'),
        'done_aging': fields.integer(string='Done Aging'),
        'due_date': fields.date(string='Due Date'),
        'avg_score': fields.integer(string='Avg Score%'),
        'score': fields.integer(string='Score %', track_visibility='onchange',),
        'top_score': fields.integer(string='Top Score%', track_visibility='onchange',),
        'remark': fields.char(string='Remark'),
        'display_name': fields.char(string='Name', compute='_compute_display_name',),
        'state' : fields.selection([('open', 'Open'), ('done', 'Done')], string='Status'),

    }

    # display_name = fields.Char(
    #         string='Name', compute='_compute_display_name',
    #     )

    @api.one
    @api.depends('student_id.name', 'quiz_id.name')
    def _compute_display_name(self):
        names = [self.student_id.name, self.quiz_id.name]
        self.display_name = ' / '.join(filter(None, names))


    _defaults = {
        'state': 'open',
    }
    def take_quiz(self, cr, uid, ids, context=None):
        import random;
        current_task = self.browse(cr, uid, ids, context=None)
        question_ids = []
        week_covered_ids = set()
        for quiz_line in current_task.quiz_id.line_ids:
            week_id = quiz_line.week_id
            week_covered_ids.add(week_id.id)
            day = quiz_line.day
            frequency = quiz_line.frequency
            vocab_options = week_id.vocab_ids.filtered(lambda r: r.day == day)
            for i in range(0,frequency):
                rand_index = random.randint(1,len(vocab_options))
                chosen_vocab_id = vocab_options[rand_index-1].id
                question_ids.append(chosen_vocab_id)

        week_covered_ids = list(week_covered_ids)
        vocab_covered_ids = self.pool.get('vocab.mean').search(cr, uid, [("week_id","in",week_covered_ids)])
        pass_context = {
            'question_ids' : question_ids,
            'week_covered_ids' : week_covered_ids,
            'vocab_covered_ids' : vocab_covered_ids,
            'question_index' : 1,
            'total_question' : len(question_ids),
            'student_id' : current_task.student_id.id,
            'student_name' : current_task.student_id.nick,
            'quiz_id' : current_task.quiz_id.id,
            # 'task_id' : current_task.id,
        }
        dummy, view_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'vocab', 'popup_quiz_form')
        return {
            'name':"Quiz",
            'view_mode': 'form',
            'view_id': view_id,
            'view_type': 'form',
            'res_model': 'popup.quiz',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context':pass_context,
        }
