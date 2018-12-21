{
    'name': 'Library Management Application',
    'description': 'Library books, members and book borrowing.',
    'author': 'Fernando',
    'depends': ['base'],
    'license': 'LGPL-3',
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/book_list_template.xml',
    ],
    'application': True,
    'installable': True
}