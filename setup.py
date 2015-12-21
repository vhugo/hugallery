from setuptools import setup, find_packages

setup(
	name='hugallery',
	version='0.1',
	description='A command line script to generate static photos gallery for Hugo (http://gohugo.io/)',
	url='http://github.com/vhugo/hugallery',
	author='Victor Alves',
	author_email='dev@sub.pro.br',
	license='MIT',
	install_requires=['Wand'],
	scripts=["hugallery"],
	zip_safe=False
)