__version__ = "0.1.0"

import pyinstaller_versionfile

package_name="file_metadata"

pyinstaller_versionfile.create_versionfile(
    output_file="versionfile.txt",
    version=__version__,
    company_name="JGStew",
    file_description=package_name,
    internal_name=package_name,
    original_filename=package_name + ".exe",
    product_name=package_name
)
