from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = '0.2'

setup(
  name = 'dudb.py',
  packages = ['dudb'],
  version = version,
  license='MIT',
  description = 'RESTful Python API Wrapper to interact with the Discord Dangerous User Database at "discord.riverside.rocks"',
  author = 'Milan Mehra',
  url = 'https://github.com/milanmdev/dudb.py',
  #download_url = 'https://github.com/milanmdev/dudb.py/tree/main/dist/dudb-' + version + '.tar.gz',
  keywords = ['dudb', 'api', 'python'],
  install_requires=[
          'requests'
  ],
  python_requires='>=3.0',
  long_description=long_description,
  long_description_content_type="text/markdown",
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
