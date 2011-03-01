##########
Python API
##########

***********************
:mod:`django_load.core`
***********************

.. module:: django_load.core

.. function:: load(modname, verbose=False, failfast=False)

    Loads modules from all installed apps.

    :param modname: Name of the module (eg: ``'plugins'``)
    :type modname: string
    :param verbose: If true, the loading will be verbose. Useful for debugging.
    :type verbose: boolean
    :param failfast: If true, the loading will not surpress exceptions.
    :type failfast: boolean
    :rtype: None

.. function:: iterload(modname, verbose=False, failfast=False)

    Same as :func:`load` but returns an iterator of the loaded modules.

    :param modname: Name of the module (eg: ``'plugins'``)
    :type modname: string
    :param verbose: If true, the loading will be verbose. Useful for debugging.
    :type verbose: boolean
    :param failfast: If true, the loading will not surpress exceptions.
    :type failfast: boolean
    :rtype: iterator of modules

.. function:: load_object(import_path)

    Loads an object from an 'import_path', like in MIDDLEWARE_CLASSES and the
    likes.
    
    Import paths should be: "mypackage.mymodule.MyObject". It then imports the
    module up until the last dot and tries to get the attribute after that dot
    from the imported module.
    
    If the import path does not contain any dots, a TypeError is raised.
    
    If the module cannot be imported, an ImportError is raised.
    
    If the attribute does not exist in the module, a AttributeError is raised.

    :param import_path: The path to the object to load, eg ``'mypackage.mymodule.MyObject'``
    :type import_path: string
    :rtype: object

.. function:: iterload_object(import_paths)

    Same as :func:`load_object` but for multiple import paths at once.
    
    :param import_paths: An iterable containing import_paths for :func:`load_object`.
    :type import_paths: iterable of strings
    :rtype: iterator of objects