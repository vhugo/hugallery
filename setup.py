from setuptools import setup, find_packages

setup(
	name='hugallery',
	version='0.1',
	description='A static web photo gallery generator for Hugo (http://gohugo.io/)',
	url='http://github.com/vhugo/hugallery',
	author='Victor Alves',
	author_email='dev@sub.pro.br',
	license='MIT',
	include_package_data=True,
	install_requires=['Wand'],
	scripts=["hugallery"],
	entry_points= {
		'console_scripts': [
			'hugallery=hugallery:main',
		],
	},
	zip_safe=False
)