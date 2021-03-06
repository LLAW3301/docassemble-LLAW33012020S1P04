import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012020S1P04',
      version='0.0.1',
      description=('Is My Complaint Covered under the Equal Opportunity Act'),
      long_description='# Is my complaint covered under the Equal Opportunity Act?\r\n\r\nAn Equal Opportunity Jurisdiction Finder created by Amelia Galpin, Holly Langford, Rebecca Rayner and Thomas Ramsey for the South Australian Equal Opportunity Commission.\r\n\r\nThe aim of our application is to allow individuals direct access to the Equal Opportunity Commission, or another relevant statutory complaints body, by asking questions to identify if the Equal Opportunity Commission would have jurisdiction to assist with the individuals complaint. \r\n',
      long_description_content_type='text/markdown',
      author='Flinders University',
      author_email='mark.ferraretto@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://eoc.sa.gov.au',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012020S1P04/', package='docassemble.LLAW33012020S1P04'),
     )

