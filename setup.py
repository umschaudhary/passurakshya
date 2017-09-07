try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [pkg.split('=')[0] for pkg in open('requirements.txt').readlines()]

setup(name='passurakshya',
      version='1.0',
      description="Save your passwords even safer : ",
      author='Umesh Chaudhary',
      author_email='umesschaudhary@gmail.com',
      url='https://github.com/umschaudhary/passurakshya',
      scripts=['src/pass'],
      install_requires=requirements,
      packages=['passurakshya'],
      package_dir = {'passurakshya': 'src/passurakshya'},
      classifiers=['Environment :: Console',
               'Programming Language :: Python :: 3' ]
      
      )
