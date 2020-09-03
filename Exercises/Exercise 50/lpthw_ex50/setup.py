try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise 50',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it',
    'author_email': 'My email.',
    'version': '0.1'
    'install_requires': ['nose', 'flask']
    'packages': ['NAME']
    'scripts': []
    'name': 'lpthw_ex50-hello_world'
}

setup(**config)
