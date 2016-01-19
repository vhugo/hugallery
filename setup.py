#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
	name='hugallery',
	version='0.1',
	description='A command line script to generate static photos gallery for Hugo (http://gohugo.io/)',
	url='http://github.com/vhugo/hugallery',
	author='Victor Alves',
	author_email='dev@sub.pro.br',
	license='MIT License',
	install_requires=['Wand'],
	scripts=["hugallery"],
	test_suite='nose.collector',
	tests_require=['nose'],
	zip_safe=False
)