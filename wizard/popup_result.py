# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class popup_result(osv.osv_memory):

    _name = 'popup.result'
    _columns = {
        'name': fields.char(string='Correct Answer'),
    }
    def fields_view_get(self, cr, uid, view_id=None, view_type='form', context={}, toolbar=False):
        result = super(popup_result, self).fields_view_get(cr, uid, view_id, view_type, context=context, toolbar=toolbar)
        vocab_task_doc = self.pool.get('vocab.task').browse(cr, uid, context['active_id'], context=None)
        if vocab_task_doc.state == 'open':
            self.pool.get('vocab.task').write(cr, uid, context['active_id'], {'state':'done', 'score': context['final_score']} )
        view_arch = result['arch']
        view_arch = view_arch.replace('SELAMAT','Congrats you have Done this , your score is  ' + str(context['final_score']))
        result['arch']= view_arch
        return result

    def complete(self, cr, uid, ids, context=None):
        return
