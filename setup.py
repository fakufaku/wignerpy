from distutils.core import setup, Extension
import os, glob, numpy



__version__ = '0.0.1'

def indir(dir, files): return [dir+f for f in files]
def globdir(dir, files):
    rv = []
    for f in files: rv += glob.glob(dir+f)
    return rv

setup(name = 'wignerpy',
    version = __version__,
    description = __doc__,
    long_description = __doc__,
    license = 'GPL',
    author = 'Joey Dumont, Jeff Zheng',
    author_email = '',
    url = '',
    package_dir = {'wignerpy':'wignerpy'},
    packages = ['wignerpy'],
    ext_modules = [
        Extension('wignerpy._wignerpy',
            globdir('wignerpy/_wignerpy/',
                ['*.cpp', '*.c', '*.cc']),
            include_dirs = ['wignerpy/_wignerpy/include', numpy.get_include()],
            extra_compile_args=['-Wno-write-strings', '-O3']
        )
    ],
    scripts = glob.glob('scripts/*'),
)

