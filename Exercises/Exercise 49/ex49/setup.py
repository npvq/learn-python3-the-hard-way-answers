try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise 49',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it',
    'author_email': 'My email.',
    'version': '0.1'
    'install_requires': ['nose']
    'packages': ['NAME']
    'scripts': []
    'name': 'lpthw_ex49-parser'
}

setup(**config)
