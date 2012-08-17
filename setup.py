# -*- coding: utf-8 -*-
### setup.py ###

from distutils.core import setup
setup (name='expeyes',
      version='1.0.0',
      description=u"a hardware & software framework for developing science experiments",
      author='Ajith Kumar B.P',
      author_email='bpajith@gmail.com',
      url='http://expeyes.in/',
      license='GPLv3',
      packages=['expeyes'],
      package_dir={'expeyes': "expeyes"},
)
