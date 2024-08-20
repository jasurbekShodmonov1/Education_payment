{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Manage courses, teachers, students, groups, and payments in a school',
    'sequence': -100,
    'description': """
        School Management System
        ========================
        This module helps in managing courses, teachers, students, groups, and payments in a school.
    """,
    'category': 'Education',
    'author': 'Jasurbek Shodmonov',
    'website': 'https://www.educationpayment1803.com',
    'depends': ['base'],
    'data': [
        'views/menu.xml',       # Menu definitions
        'views/course_view.xml',     # Course views and actions.xml
        'views/teacher_view.xml',    # Teacher views and actions.xml
        'views/student_view.xml',    # Student views and actions.xml
        'views/group_view.xml',      # Group views and actions.xml
        'views/payment_view.xml',    # Payment views and actions.xml
        'security/ir.model.access.csv', # Access control
        'security/security.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
