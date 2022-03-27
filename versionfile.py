
# import setuptools.config

import pyinstaller_versionfile

# https://www.programcreek.com/python/example/123119/setuptools.config.read_configuration
#config_parsed = setuptools.config.read_configuration("setup.cfg").get("metadata", {})
# package_name = config_parsed["name"]
# package_author = config_parsed["author"]
# __version__ = config_parsed["version"]

from _version import version as __version__

package_name = "file_metadata"
package_author = "JGStew"

pyinstaller_versionfile.create_versionfile(
    output_file="versionfile.txt",
    version=__version__,
    company_name=package_author,
    file_description=package_name,
    internal_name=package_name,
    original_filename=package_name + ".exe",
    product_name=package_name
)
