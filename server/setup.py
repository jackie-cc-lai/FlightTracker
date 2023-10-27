from setuptools import setup

setup(
    name='flight_BE',
    packages=['config', 'routes', 'service'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
