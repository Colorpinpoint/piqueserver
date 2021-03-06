
# to have global configuration variables
# similar to
# http://effbot.org/pyfaq/how-do-i-share-global-variables-across-modules.htm

import os
import sys

# pylint: disable=invalid-name

server_version = '%s - %s' % (sys.platform, '0.0.1a')
config = {}
pkg_name = "piqueserver"
config_file = 'config.json'

config_path = os.environ.get('XDG_CONFIG_HOME', '~/.config') + "/piqueserver"
config_dir = os.path.expanduser(config_path)

# filled from command line argument
json_parameters = ""
