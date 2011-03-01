# -*- coding: utf-8 -*-
from __future__ import with_statement
from django_load.core import load, iterload, load_object, iterload_objects
from testproject.core import pool
from unittest import TestCase
import sys
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO


class StdoutOverride(object):
    def __init__(self):
        self.buffer = StringIO()
        
    def __enter__(self):
        sys.stdout = self.buffer
        return self.buffer
        
    def __exit__(self, type, value, traceback):
        sys.stdout = sys.__stdout__
    

class DjangoLoad(TestCase):
    def setUp(self):
        pool.clear()
        self.old_modules = dict(sys.modules)
        
    def tearDown(self):
        """
        Reset imports
        """
        for key in sys.modules.keys():
            if key not in self.old_modules:
                del sys.modules[key]
        
    def test_plugins(self):
        load('plugins')
        self.assertTrue('plugins' in pool, pool)
        self.assertEqual(len(pool['plugins']), 2, pool)
        self.assertEqual(sorted(pool['plugins']), sorted(['everything', 'plugin']))
        
    def test_extensions(self):
        load('extensions')
        self.assertTrue('extensions' in pool, pool)
        self.assertEqual(len(pool['extensions']), 2, pool)
        self.assertEqual(sorted(pool['extensions']), sorted(['everything', 'package']))
    
    def test_failfast(self):
        self.assertRaises(ImportError, load, 'plugins', failfast=True)
        
    def test_verbose(self):
        with StdoutOverride() as buffer:
            load('plugins', verbose=True)
            buffer.seek(0)
            output = buffer.getvalue()
        self.assertEqual(output.count('Loaded'), 2)
        self.assertEqual(output.count('Could not load'), 3)
        
    def test_iter(self):
        modules = list(iterload('plugins'))
        self.assertEqual(len(modules), 2)
        self.assertTrue('plugins' in pool, pool)
        self.assertEqual(len(pool['plugins']), 2, pool)
        self.assertEqual(sorted(pool['plugins']), sorted(['everything', 'plugin']))
        
    def test_load_object(self):
        obj = load_object('testproject.everything.models.MyObject')
        self.assertEqual(obj.app_name, 'everything')
        
    def test_load_object_fail_type(self):
        self.assertRaises(TypeError, load_object, 'myimportpath')
        
    def test_load_object_fail_import(self):
        self.assertRaises(ImportError, load_object, 'my.import.path')
        
    def test_load_object_fail_attribute(self):
        self.assertRaises(AttributeError, load_object, 'testproject.nothing.models.MyObject')
        
    def test_iterload_objects(self):
        objs = list(iterload_objects(['testproject.everything.models.MyObject']))
        self.assertEqual(len(objs), 1)
        self.assertEqual(objs[0].app_name, 'everything')