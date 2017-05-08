# $HOME/.config/sublime-text-3/Packages/node-env.py

import os
import getpass

nvm_path = '/home/%(user)s/.nvm' % {'user': getpass.getuser()}
nvm_default_file_path = '%(root)s/alias/default' % {'root': nvm_path}
nvm_node_root = '%(root)s/versions/node' % {'root': nvm_path}

# Grab default alias
with open(nvm_default_file_path, 'r') as content_file:
    content = content_file.read()

# Prepend 'v' to match folder names
version = content.strip()
if version[0] != 'v':
  version = 'v' + version

# Take highest valid folder name
versions = os.listdir(nvm_node_root)
found = sorted([v for v in versions if v.startswith(version)])[-1]

if found == None:
  print("Failed to configure node: no valid version found for %(version)s" % {'version': version})
else:
  print("Configure node: %(version)s" % {'version': found})
  node_path = "%(root)s/%(version)s" % {'root': nvm_node_root, 'version': found }
  print("Node path: %(root)s" % {'root': node_path})
  path = "%(root)s/bin:%(root)s/lib:%(path)s" % {'root':node_path, 'path':os.environ["PATH"]}
  os.environ["PATH"] = path
