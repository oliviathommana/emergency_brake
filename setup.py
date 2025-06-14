
packages=['emergency_brake'],
entry_points={
    'console_scripts': [
        'emergency_brake_node = emergency_brake.emergency_brake_node:main',
    ],
},
from setuptools import setup

package_name = 'emergency_brake'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='Emergency Brake Node',
    entry_points={
        'console_scripts': [
            'emergency_brake_node = emergency_brake.emergency_brake_node:main',
        ],
    },
)
