from setuptools import setup
import re

VERSIONFILE = "./_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

print(f"========> Current version is {verstr}")

setup(name='jama_rest_client',
      version=verstr,
      description='Jama REST client',
      url='https://github.com/Tanaka12/jama-rest-client',
      author='Jose Peiro',
      packages=['jama_rest_client',
                'jama_rest_client.api',
                'jama_rest_client.dal',
                'jama_rest_client.dal.parsers',
                'jama_rest_client.dal.parsers.json',
                'jama_rest_client.http',
                'jama_rest_client.model',
                'jama_rest_client.model.api_response',
                'jama_rest_client.model.http',
                'jama_rest_client.model.item',
                'jama_rest_client.model.item_type',
                'jama_rest_client.model.location',
                'jama_rest_client.model.lock',
                'jama_rest_client.model.project',
                'jama_rest_client.model.test_cycle',
                'jama_rest_client.model.test_plan',
                'jama_rest_client.model.test_run',
                'jama_rest_client.utils',
                'jama_rest_client.utils.authorization'],
      classifiers=[
          "Topic :: Jama :: REST :: client",
          "Programming Language :: Python :: 3",
          "License :: Free"],
      install_requires=[],
      tests_require=['pytest==8.2.2',
                     'pytest-mock==3.14.0'],
      zip_safe=False
)
