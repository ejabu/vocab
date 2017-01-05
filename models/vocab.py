# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class vocab_week(osv.osv):

    _name = 'vocab.week'
    _description = 'Form for updating Vocab weekly'
    _columns = {
        'name': fields.char(string='Name'),
        'published_date': fields.date(string='Published Date'),
        'vocab_ids': fields.one2many('vocab.mean', 'week_id', 'Vocabularies'),
    }
class vocab_mean(osv.osv):

    _name = 'vocab.mean'
    _description = 'Form for updating Vocab weekly'
    _columns = {
        'name': fields.char(string='ID'),
        'english': fields.char(string='English'),
        'arabic': fields.char(string='Arabic'),
        'published_date': fields.date(string='Published Date'),
        'week_id': fields.many2one('vocab.week', 'Week', readonly=True),
    }
