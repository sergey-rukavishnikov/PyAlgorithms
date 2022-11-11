from setuptools import setup, find_packages

setup(name='MyAlgorithms',
      version='0.1',
      url='https://github.com/sergey-rukavishnikov/PyAlgorithms.git',
      license='MIT',
      author='Sergey Rukavishnikov',
      author_email='sergeyruk312@gmail.com',
      description='Algorithms written by me',
      packages=find_packages(exclude=['test_MyAlgorithms']),
      long_description=open('C:\\Users\\serge\\PycharmProjects\\MyAlgorithms\\README.md').read(),
      zip_safe=False)
