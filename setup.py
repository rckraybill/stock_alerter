try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'TDD Stock Tests Demo',
    'author': 'Ross Kraybill',
    'url': 'url',
    'download_url': 'download_url',
    'author_email': 'rckraybill@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['stock'],
    'scripts': [],
    'name': 'stock'
}

setup(**config)
