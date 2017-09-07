try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='passurakshya',
      version='2.0.1',
      description="Save your passwords even safer : ",
      author='Umesh Chaudhary',
      author_email='umesschaudhary@gmail.com',
      url='https://github.com/umschaudhary/passurakshya',
      scripts=['src/passurakshya'],
      packages=['passurakshya'],
      package_dir = {'passurakshya': 'src/pasurakshya'},
      classifiers=['Environment :: Console',
               'Programming Language :: Python :: 3' ]
      
      )
