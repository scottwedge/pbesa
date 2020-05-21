from distutils.core import setup
setup(
  name = 'pbesa',
  packages = ['pbesa'],
  version = '1.0',
  license='MIT',
  description = 'An artificial intelligence platform for the implementation of multi-agent systems based on python 3 and the BESA model',
  author = 'Enrique Gonzales Guerreo, Cesar Julio Bustacara, Fabian Jose Roldan',
  author_email = 'egonzal@javeriana.edu.co, cbustaca@javeriana.edu.co, fjroldan@akenfactory.com',
  url = 'https://github.com/akenfactory/pbesa.git',
  download_url = 'https://github.com/akenfactory/pbesa.git/archive/pypi-0_1_3.tar.gz',
  keywords = ['agent', 'multi-agent', 'system', 'artificial', 'intelligence'],
  install_requires=[
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 5 - Production/Stable',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)