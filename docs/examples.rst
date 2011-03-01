########
Examples
########

****
load
****

Let's assume your app wants to load all ``plugins.py`` files from the installed
apps, to allow those apps to extend your application. You can achieve this like
this::

    from django_load.core import load
    
    load('plugins')
    
********
iterload
********

Now let's say you want to do the same, but actually do something with those
modules, more specific, find all objects in those modules, that are subclasses
of ``BasePlugin`` and call our ``do_something`` function with those objects::

    from django_load.core import iterload
    
    for module in iterload('plugins'):
        for name in dir(module):
            obj = getattr(module, name)
            if issubclass(obj, BasePlugin):
                do_something(obj)

****************
iterload_objects
****************

You could also have a setting called ``MY_APP_PLUGINS`` which contains import
paths similar to ``MIDDLEWARE_CLASSES``. You want to load those plugins and
call the ``do_something`` function with them::


    from django_load.core import iterload_objects
    from django.conf import settings
    
    for obj in iterload_objects(settings.MY_APP_PLUGINS):
        do_something(obj)

***********
load_object
***********

If you only want to load a single object, you can do that too. Let's say you 
want to load ``MyObject`` from the ``mypackage.mymodule`` module::

    from django_load.core import load_object
    
    obj = load_object('mypackage.mymodule.MyObject')