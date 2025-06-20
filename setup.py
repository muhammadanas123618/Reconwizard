from setuptools import setup, find_packages

setup(
    name='reconwizard',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'dnspython',
        'python-whois',
        'requests',
        'jinja2',
        'click'
    ],
    entry_points='''
        [console_scripts]
        reconwizard=reconwizard.cli:main
    ''',
)
