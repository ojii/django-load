from setuptools import setup, find_packages

version = __import__('django_load').__version__

setup(
    name = 'django-load',
    version = version,
    description = 'Module loader for Ajango apps.',
    author = 'Jonas Obrist',
    author_email = 'jonas.obrist@divio.ch',
    url = 'http://github.com/ojii/django-load',
    packages = find_packages(),
    zip_safe=False,
    install_requires=[
        'django>=1.2',
    ],
    test_suite='django_load.tests',
)
