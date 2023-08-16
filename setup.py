import setuptools

# setup has to be layed out correctly or you cannot make a package using the 
# 'python setup.py sdist bdist_wheel' command

setuptools.setup(
    name='hellow-world',
    version= '0.0.1',
    author= 'andy',
    description= 'prints hello world',
    py_modules= ['hello_world'],
    package_die={'': 'hello-world-package/src'}) #package key is empty for some reason