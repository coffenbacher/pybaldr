from setuptools import setup

setup(name='pybaldr',
      version='0.1',
      description='Python library to read the Baldr format from uSwitch',
      url='http://github.com/coffenbacher/pybaldr',
      author='coffenbacher',
      license='MIT',
      packages=['pybaldr',],
      install_requires=[
          #'beautifulsoup4',
      ],
      dependency_links=[
            #https://github.com/laurentb/weboob/
      ],
      zip_safe=False)
