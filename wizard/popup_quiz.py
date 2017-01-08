# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class popup_quiz(osv.osv_memory):

    _name = 'popup.quiz'
    _columns = {
        'name': fields.char(string='Name'),
    }
    def take_quiz(self, cr, uid, ids, context=None):
        # self.write(cr, uid, ids, {'state': 'close'}, context=context)
        # return
        dummy, view_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'vocab', 'popup_quiz_form') #in model name replace . with _ Example sale.order become sale_order
        import ipdb; ipdb.set_trace()
        return {
            'name':"Quiz",
            'view_mode': 'form',
            'view_id': view_id,
            'view_type': 'form',
            'res_model': 'popup.quiz',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'nodestroy': False,
        }
