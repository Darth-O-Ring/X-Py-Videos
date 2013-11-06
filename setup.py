#!/usr/bin/env python2
from distutils.core import setup
from os import remove
from os.path import abspath
from os.path import join as path_join
from os import getcwd
from shutil import copyfile, rmtree
from os import remove

pathname		=		getcwd()

copyfile("xpyvideos.py", "xpyvideos/xpyvideos")

setup(name		=		'xpyvideos',
      version		=		'0.0.2-7',
      description	=		'Python program for downloading videos from xvideos, xhamster, and redtube.',
      author		=		'Darth_O-Ring',
      author_email	=		'darthoring@gmail.com',
      url		=		'https://github.com/Darth-O-Ring/xpyvideos',
      packages		=		['xpyvideos'],
      package_dir	=		{'xpyvideos' : 'xpyvideos/'},
      scripts		=		['xpyvideos/xpyvideos'],
      data_files	=		[('share/xpyvideos', ['README.md', 'NOTICE'])],

	)

files		=		['/usr/bin/opts.py', '/usr/bin/filename.py', '/usr/bin/download.py', '/usr/bin/regexes.py',
					'/usr/bin/xpyvideos.py', 'xpyvideos/xpyvideos']

for i in xrange(len(files)):
	try:
		if '/usr/bin/' in files[i]:
			remove(abspath(files[i]))
		else:
			remove(abspath(path_join(pathname, files[i])))
	except:
		pass

try:
	rmtree(abspath(path_join(pathname, 'build/')))
except:
	pass
