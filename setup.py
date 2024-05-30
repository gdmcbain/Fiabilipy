#!/usr/bin/env python

from distutils.core import setup

setup(name='fiabilipy',
      version='3.2',
      description='Learn engineering reliability with python',
      long_description=open('README.md').read(),
      author='Simon Chabot, Akim Sadaoui, Vincent Lecrubier',
      author_email='contact@fiabilipy.org',
      url='https://pythonhosted.org/fiabilipy',
      license='GPLv2+',
      keywords=('dependability', 'availability', 'reliability', 'markov'),
      requires=['numpy', 'scipy', 'sympy', 'networkx','future'],
      packages=['fiabilipy'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Education',
          'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
          'Topic :: Scientific/Engineering',
      ]
     )
