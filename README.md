# django_setting_sample_project
APISettings sample for study.

## Installation
1. clone
2. Init venv
3. Install requirements.txt
4. Generate secret key like this:
```bush
  python generate_secretkey.py >> config/settings.py
```

5. Migrate
6. Create super user.
7 Run server.

## Usage
Try change config/settings.py. like this:
```python
  ...
  TODO_API = {
      # if you want change status choices.
      'TASK_STATUS_CHOICES': [
          (1, 'TODO'),
          (2, 'DOING'),
          (3, 'DONE'),
          (4, 'NEW_STATUS'),
      ],
      
      # if you want change permissions
      'TASK_PERMISSIONS': []
  }
```
