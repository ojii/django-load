# Django settings for testproject project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'testproject.nothing',
    'testproject.plugins',
    'testproject.everything',
    'testproject.package',
    'django_load',
)
