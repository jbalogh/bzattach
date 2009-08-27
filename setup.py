from distutils.core import setup

requirements = open('reqs.txt').read.split()

setup(name='bzattach',
      version='0.3',
      scripts=['bzattach'],
      install_requires=requirements,
)
