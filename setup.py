# flake8: noqa

from setuptools import setup, find_packages

setup(
    name="tbsignal",
    version='0.2.0',
    description="Angelcam traceback signal handler",
    keywords="traceback signal",
    author="Angelcam",
    author_email="dev@angelcam.com",
    url="https://bitbucket.org/angelcam/python-traceback-signal/",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5'
    ]
)
