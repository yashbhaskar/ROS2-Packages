from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'simple_pkg_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share",package_name,"launch"),glob("launch/*")),
        (os.path.join("share",package_name,"scripts"),glob("scripts/*")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yash',
    maintainer_email='yash@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'talker = simple_pkg_python.pub:main',
        	'listener = simple_pkg_python.sub:main',
            'param = simple_pkg_python.parameter_handling:main',
        ],
    },
)
