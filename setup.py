from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='whatisthis',
      version='0.0.1',
      description='',
      long_description=readme(),
      url='http://github.com/Tom-Alexander/whatisthis',
      download_url = 'https://github.com/peterldowns/mypackage/tarball/0.0.1',
      author='Tom Alexander',
      author_email='me@tomalexander.co.nz',
      license='MIT',
      packages=['whatisthis'],
      include_package_data=True,
      zip_safe=False)
