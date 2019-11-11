from utils.app_setting import APISettings

DEFAULTS = {
    'TASK_TITLE_MAX_LENGTH': 30,
    'TASK_STATUS_CHOICES': [
        (1, 'TODO'),
        (2, 'DOING'),
        (3, 'DONE'),
    ],
    'TASK_PERMISSIONS': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}

api_settings = APISettings('TODO_API', DEFAULTS)
