from distutils.core import setup

setup(
    name = 'mypassword',
    packages = ['mypassword'],
    version = '0.0.1',
    description = 'Tools for generating strong passwords',
    author = 'Vicente Gutiérrez',
    author_email = 'vinzegtz@gmail.com',
    url = 'https://github.com/vinzegtz/mypassword',
    download_url = 'https://github.com/vinzegtz/mypassword/archive/v0.0.1-beta.tar.gz',
    keywords = ['password', 'pass', 'password-manager'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Security',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)