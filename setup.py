from setuptools import setup
from commen5 import __version__

setup(
    name='django-commen5',
    version=__version__,
    description="django-commen5 creates a comment template tag named: commen5",
    long_description=open('README.rst').read(),
    author='Brad Montgomery',
    author_email='brad@bradmontgomery.net',
    url='https://github.com/bradmontgomery/django-commen5/',
    license='MIT',
    packages=['commen5'],
    include_package_data=True,
    package_data={'': ['README.rst']},
    zip_safe=False,
    install_requires=['django', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Markup :: HTML',
        'Intended Audience :: Developers',
    ]
)
