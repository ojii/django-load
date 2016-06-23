from setuptools import setup, find_packages

version = __import__('django_load').__version__

setup(
    name = 'django-load',
    version = version,
    description = 'Module loader for Django apps.',
    author = 'Jonas Obrist',
    author_email = 'ojiidotch@gmail.com',
    url = 'http://github.com/ojii/django-load',
    packages = find_packages(),
    license='BSD',
    zip_safe=False,
    install_requires=[
        'django>=1.2',
    ],
    test_suite='django_load.tests',
)
