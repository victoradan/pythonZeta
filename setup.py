from setuptools import setup
from setuptools import find_packages

setup(name='pyZeta',
      description='FP for Python',
      long_description='FP for Python',
      version='0.0.1',
      author='vctradn@gmail.com',
      author_email='vctradn@gmail.co',
      url='',
      license='MIT',
      platforms=['linux', 'osx'],
      packages=find_packages(),
      install_requires=['toolz==0.9.0'],
      tests_require=[],
      classifiers=[
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3.6',
          ],
      )
