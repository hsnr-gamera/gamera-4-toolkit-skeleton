from pathlib import Path

from setuptools import setup

from gamera import gamera_setup

# This constant should be the name of the toolkit
TOOLKIT_NAME = "skeleton"

# ----------------------------------------------------------------------------
# You should not usually have to edit anything below, but it is
# implemented here and not in the Gamera core so that you can edit it
# if you need to do something more complicated (for example, building
# and linking to a third- party library).
# ----------------------------------------------------------------------------

PLUGIN_PATH = 'gamera/toolkits/%s/plugins/' % TOOLKIT_NAME
PACKAGE = 'gamera.toolkits.%s' % TOOLKIT_NAME
PLUGIN_PACKAGE = PACKAGE + ".plugins"
plugins = gamera_setup.get_plugin_filenames(PLUGIN_PATH)
plugin_extensions = gamera_setup.generate_plugins(plugins, PLUGIN_PACKAGE)

# find gamera include directory
gamera_include = Path(gamera_setup.__file__).parent.joinpath("include/gamera").__str__()

# This is a standard distutils setup initializer.  If you need to do
# anything more complex here, refer to the Python distutils documentation.
setup(name=TOOLKIT_NAME,
      version="4.1.0",
      ext_modules=plugin_extensions,
      include_dirs=[gamera_include],
      packages=[PACKAGE, PLUGIN_PACKAGE],
      scripts=['scripts/skeleton'],
      install_requires=['gamera>=4.1.0']
      )
