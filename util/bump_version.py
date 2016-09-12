import re
import sys

# Sanity checks on the command line args.  A bit ugly, but still straightforward
# enough that I don't feel the need to bring in argparse.
assert len(sys.argv) > 1, 'Specify a bump type.  Bump types must be one of {major, minor, patch}.'
bump_type =  sys.argv[1].lower()
assert bump_type in ['major', 'minor', 'patch'], 'Requested bump type ({0}) is not valid.  Bump types must be one of {{major, minor, patch}}.'.format(bump_type)

# Read/parse/split the existing version string.
with open('VERSION') as f_in:
    old_version = f_in.read().strip()
    
print 'Old version is:  {0}'.format(old_version)

# The existing version is expected to follow a simple
# major.minor.patch format.   See http://semver.org/
m = re.search('^(\d+)\.(\d+)\.(\d+)$', old_version)

# If the input wasn't in the expected format, just give up.
assert m, 'Existing VERSION string is not in the correct format.'

# Parse the existing values.
major_version = int(m.group(1))
minor_version = int(m.group(2))
patch_version = int(m.group(3))

# Update the values based on the requested bump type.
if bump_type == 'major':
    major_version = major_version + 1
    minor_version = 0
    patch_version = 0
elif bump_type == 'minor':
    minor_version = minor_version + 1
    patch_version = 0
elif bump_type == 'patch':
    patch_version = patch_version + 1

# Construct the new version string.
new_version = '{0}.{1}.{2}'.format(major_version, minor_version, patch_version)

print 'New version is:  {0}'.format(new_version)

# Write the new version back to the version file.
with open('VERSION', 'w') as f_out:
    f_out.write(new_version)