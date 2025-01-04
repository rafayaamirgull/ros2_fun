from setuptools import find_packages, setup

package_name = 'pub_sub_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rafay',
    maintainer_email='rafay.aamir.gull@gmail.com',
    description='Publisher Subcriber in python with ROS2',
    license='License01012025',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['talker = pub_sub_python.publisher:main',
                            'listener = pub_sub_python.subscriber:main',
        ],
    },
)
