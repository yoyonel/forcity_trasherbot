# -*- encoding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

# https://docs.python.org/3/distutils/setupscript.html
setup(
    name='forcity-trasherbot',
    version='1.0.0',
    license='None',
    description='',
    author='Lionel Atty',
    author_email='yoyonel@hotmail.com',
    url='https://github.com/yoyonel/forcity_trasherbot.git',
    packages=['forcity.{}'.format(x) for x in find_packages('src/forcity')],
    package_dir={'': 'src'},
    # package_data={},
    # include_package_data=True,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    keywords=[

    ],
    install_requires=[
        "bresenham==0.2",
        "dataclasses==0.6",
        "jsonschema==2.6.0",
        "numpy==1.15.4",
    ],
    extras_require={},
    entry_points={
        'console_scripts': [
            'trasherbot = forcity.trasherbot.app:main'
        ]
    },
    python_requires='>=3.6'
)
