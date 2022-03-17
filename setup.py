from setuptools import setup

setup(
   name='MyWebApp',
   version='1.0',
   description='A useful module',
   author='s.lu',
   author_email='shanswork@yahoo.com',
   packages=['MyWebApp'],  #same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
)