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
    def take_quiz(self, cr, uid, ids, context=None):
        # self.write(cr, uid, ids, {'state': 'close'}, context=context)
        # return
        dummy, view_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'vocab', 'popup_quiz_form') #in model name replace . with _ Example sale.order become sale_order
        import ipdb; ipdb.set_trace()
        return {
            'name':"Quiz",#Name You want to display on wizard
            'view_mode': 'form',
            'view_id': view_id,
            'view_type': 'form',
            'res_model': 'popup.quiz',# With . Example sale.order
            # 'res_model': 'account.chart',# With . Example sale.order
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
