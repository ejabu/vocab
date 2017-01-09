# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class popup_quiz(osv.osv_memory):

    _name = 'popup.quiz'
    _columns = {
        'name': fields.char(string='Name'),
        'correct': fields.char(string='Correct Answer'),
    }
    # def default_get(self, cr, uid, fields, context=None):
    #     res = super(popup_quiz, self).default_get(cr, uid, fields, context=context)
    #     import ipdb; ipdb.set_trace()
    #     res.update({'name':'jaj'})
    #     # data = self.trans_rec_get(cr, uid, context['active_ids'], context)
    #     # if 'trans_nbr' in fields:
    #     #     res.update({'trans_nbr':data['trans_nbr']})
    #     # if 'credit' in fields:
    #     #     res.update({'credit':data['credit']})
    #     # if 'debit' in fields:
    #     #     res.update({'debit':data['debit']})
    #     # if 'writeoff' in fields:
    #     #     res.update({'writeoff':data['writeoff']})
    #     return res


    # def create(self, cr, uid, vals, context=None):
    #     import ipdb; ipdb.set_trace()
    #     return super(popup_quiz, self).create(cr, uid, vals, context=context)
    #
    #
    # def view_init(self, cr, uid, fields_list, context=None):
    #     res = super(popup_quiz, self).view_init(cr, uid, fields_list, context=context)
    #     import ipdb; ipdb.set_trace()
    #     return res

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
    def answer_quiz(self, cr, uid, ids, context=None):
        # self.write(cr, uid, ids, {'name':'haha'})
        import ipdb; ipdb.set_trace()
        if 'correct' in context:
            print 'jawaban benar'
        return
        # return



    def fields_view_get(self, cr, uid, view_id=None, view_type='form', context={}, toolbar=False):
        result = super(popup_quiz, self).fields_view_get(cr, uid, view_id, view_type, context=context, toolbar=toolbar)
        # print result;

        week_covered_ids = context["week_covered_ids"]
        vocab_covered_ids = context["vocab_covered_ids"]
        removed_vocab_covered_ids = context["vocab_covered_ids"]
        question_ids = context["question_ids"]
        question_index = context["question_index"]
        total_question = context["total_question"]

        if question_index > total_question:
            print "done"
            return
        import random
        question_to_ask = question_ids[question_index-1]
        removed_vocab_covered_ids.remove(question_to_ask)
        random.shuffle(removed_vocab_covered_ids)
        false_option = removed_vocab_covered_ids[:3]



        false_option.append(question_to_ask)
        mixed_options = false_option
        random.shuffle(mixed_options)


        lang_index = random.randint(0,1)
        question_lang = ['english','arabic'][lang_index]
        answer_lang = ['english','arabic'][0 if lang_index == 1 else 1]


        # import ipdb; ipdb.set_trace()
        vocab_mean_obj = self.pool.get('vocab.mean')
        view_arch = result['arch']

        vocab_mean_doc = vocab_mean_obj.browse(cr,uid, question_to_ask, context=None)
        view_arch = view_arch.replace('SOALSOAL',vocab_mean_doc[question_lang])


        for option in range(0,4):

            vocab_mean_doc = vocab_mean_obj.browse(cr,uid, mixed_options[option], context=None)

            # import ipdb; ipdb.set_trace()

            if question_to_ask == mixed_options[option]:
                view_arch = view_arch.replace(['Option A','Option B','Option C','Option D'][option],vocab_mean_doc[answer_lang]+'''" context="{'correct':'true'} ''')
            else:
                view_arch = view_arch.replace(['Option A','Option B','Option C','Option D'][option],vocab_mean_doc[answer_lang])
            print 'hehe'


        # old = result['arch']
        # new = result['arch'].replace('Thank','HAHA').replace('DemoClass','DemoClass2')
        result['arch']= view_arch
        # your modification in the view
        # result['fields'] will give you the fields. modify it if needed
        # result['arch'] will give you the xml architecture. modify it if needed
        import ipdb; ipdb.set_trace()
        return result
