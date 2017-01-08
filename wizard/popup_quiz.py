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
            'context':{'haha': 'ejaa'},
        }

    def fields_view_get(self, cr, uid, view_id=None, view_type='form', context={}, toolbar=False):
        result = super(popup_quiz, self).fields_view_get(cr, uid, view_id, view_type, context=context, toolbar=toolbar)
        # print result;
        import ipdb; ipdb.set_trace()
        old = result['arch']
        new = result['arch'].replace('Thank','HAHA').replace('DemoClass','DemoClass2')
        result['arch']=new
        # your modification in the view
        # result['fields'] will give you the fields. modify it if needed
        # result['arch'] will give you the xml architecture. modify it if needed
        return result
