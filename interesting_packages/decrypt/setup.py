from setuptools import setup, find_packages
from setuptools.command.install import install

from poc.main import runner


class Installer(install):
    def run(self):
        runner()
        install.run(self)


setup(
    name="poc",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    cmdclass={'install': Installer}
)
