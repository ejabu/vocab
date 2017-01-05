# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class vocab_week(osv.osv):

    _name = 'vocab.week'
    _description = 'Form for updating Vocab weekly'
    _columns = {
        'name': fields.char(string='Name'),
        'published_date': fields.date(string='Published Date'),
    }
