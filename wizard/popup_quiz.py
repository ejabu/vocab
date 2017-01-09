# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class popup_quiz(osv.osv_memory):

    _name = 'popup.quiz'
    _columns = {
        'question_index': fields.char(string='Question Index'),
        'correct': fields.char(string='Correct Answer'),
    }
    def default_get(self, cr, uid, fields, context=None):
        res = super(popup_quiz, self).default_get(cr, uid, fields, context=context)
        res.update({'question_index':context['question_index']})
        return res

    def take_quiz(self, cr, uid, ids, context=None):
        dummy, view_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'vocab', 'popup_quiz_form') #in model name replace . with _ Example sale.order become sale_order
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
        question_index = self.browse(cr,uid, ids, context).question_index
        dummy, view_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'vocab', 'popup_quiz_form')
        context['question_index']=int(context['question_index']) + 1
        if 'correct' in context:
            if context['correct'] == "true":
                context['correct'] = "false"
                return {
                    'name':"Quiz Jawaban Benar",
                    'view_mode': 'form',
                    'view_id': view_id,
                    'view_type': 'form',
                    'res_model': 'popup.quiz',
                    'type': 'ir.actions.act_window',
                    'target': 'new',
                    'context': context,
                }
            else:
                return {
                    'name':"Quiz Jawaban Salah",
                    'view_mode': 'form',
                    'view_id': view_id,
                    'view_type': 'form',
                    'res_model': 'popup.quiz',
                    'type': 'ir.actions.act_window',
                    'target': 'new',
                    'context': context,
                }
        else:
            return {
                'name':"Quiz Jawaban Salah",
                'view_mode': 'form',
                'view_id': view_id,
                'view_type': 'form',
                'res_model': 'popup.quiz',
                'type': 'ir.actions.act_window',
                'target': 'new',
                'context': context,
            }

    def fields_view_get(self, cr, uid, view_id=None, view_type='form', context={}, toolbar=False):
        import random
        result = super(popup_quiz, self).fields_view_get(cr, uid, view_id, view_type, context=context, toolbar=toolbar)

        week_covered_ids = context["week_covered_ids"]
        vocab_covered_ids = context["vocab_covered_ids"]
        removed_vocab_covered_ids = context["vocab_covered_ids"]
        question_ids = context["question_ids"]
        question_index = context["question_index"]
        total_question = context["total_question"]
        if question_index > total_question:
            print "done"
            return
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

        vocab_mean_obj = self.pool.get('vocab.mean')
        view_arch = result['arch']
        vocab_mean_doc = vocab_mean_obj.browse(cr,uid, question_to_ask, context=None)
        view_arch = view_arch.replace('SOALSOAL',vocab_mean_doc[question_lang])
        for option in range(0,4):
            vocab_mean_doc = vocab_mean_obj.browse(cr,uid, mixed_options[option], context=None)
            if question_to_ask == mixed_options[option]:
                # print ['Option A','Option B','Option C','Option D'][option]
                view_arch = view_arch.replace(['Option A','Option B','Option C','Option D'][option],vocab_mean_doc[answer_lang]+'''" context="{'correct':'true'} ''')
            else:
                view_arch = view_arch.replace(['Option A','Option B','Option C','Option D'][option],vocab_mean_doc[answer_lang])
        result['arch']= view_arch
        return result
