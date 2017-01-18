# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp import api

class vocab_mean(osv.osv):

    _name = 'vocab.mean'
    _description = 'Form for updating Vocab weekly'
    _columns = {
        'name': fields.char(string='ID'),
        'day': fields.integer(string='Day'),
        'english': fields.char(string='English'),
        'arabic': fields.char(string='Arabic'),
        'published_date': fields.date(string='Published Date'),
        'week_id': fields.many2one('vocab.week', 'Week', readonly=True),
    }
