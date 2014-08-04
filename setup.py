from setuptools import setup

setup(name='sphinx-api-any',
      version='0.1',
      description='extract comments from source files into rst files',
      url='https://github.com/tlamadon/sphinx-api-any',
      author='Thibaut Lamadon',
      author_email='thibaut.lamadon@gmail.com',
      license='MIT',
      packages=['sphinx-api-any'],
      scripts=['bin/sphinx-api-any'],
      zip_safe=False)