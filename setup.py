from distutils.core import setup

setup(
    name = 'boltiot',
    packages = ['boltiot'],
    version = '1.11.2',
    install_requires=['twilio','requests'],
    description = 'A Python module for communicating with the Bolt Cloud API.',
    author = 'Inventrom Pvt. Ltd.',
    author_email  = 'support@boltiot.com',
    url = 'https://github.com/Inventrom/bolt-api-python',
    download = 'https://github.com/Inventrom/bolt-api-python/archive/1.11.2.tar.gz',
    keywords = ['iot-platform','bolt','bolt-python'],
    classifiers = []
    )
