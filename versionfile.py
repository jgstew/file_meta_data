
import pyinstaller_versionfile

import setuptools.config
# https://www.programcreek.com/python/example/123119/setuptools.config.read_configuration
config_parsed = setuptools.config.read_configuration("setup.cfg").get("metadata", {})
package_name = config_parsed["name"]
__version__ = config_parsed["version"]

pyinstaller_versionfile.create_versionfile(
    output_file="versionfile.txt",
    version=__version__,
    company_name=config_parsed["author"],
    file_description=package_name,
    internal_name=package_name,
    original_filename=package_name + ".exe",
    product_name=package_name
)
