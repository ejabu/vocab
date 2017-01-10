{
    "name": "Vocabulary Learning",
    "version": "1.0",
    "depends": ['base', 'mail'],
    'author': 'Muhammad Fahreza',
    "category":"Vocabulary Learning",
    "description" : """Module to help learning process of vocabularies""",
    'data': [
        'static_file.xml',
        'views/menus.xml',
        'views/vocab_week_view.xml',
        'views/vocab_mean_view.xml',
        'views/vocab_quiz_view.xml',
        'views/vocab_task_view.xml',
        'views/mahad_student_view.xml',
        'views/mahad_era_view.xml',
        'wizard/popup_quiz_view.xml',
        'wizard/popup_result_view.xml',
    ],
    'demo':[
            #files containing demo data
    ],
    'test':[
            #files containing tests
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,

}
