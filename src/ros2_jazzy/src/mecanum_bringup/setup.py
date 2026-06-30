from setuptools import setup
from glob import glob

package_name = "mecanum_bringup"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        (
            "share/ament_index/resource_index/packages",
            ["resource/" + package_name],
        ),
        (
            "share/" + package_name,
            ["package.xml"],
        ),
        (
            "share/" + package_name + "/launch",
            glob("launch/*.py"),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Dibyanshu",
    maintainer_email="example@example.com",
    description="Bringup package",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
           "cmd_vel_bridge = mecanum_bringup.cmd_vel_bridge:main", 
           "tf_odom_bridge = mecanum_bringup.tf_odom_bridge:main",
        ],
    },
)
