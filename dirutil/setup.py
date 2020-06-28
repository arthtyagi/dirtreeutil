import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='dirtreeutil',  
     version='0.1.1',
     scripts=['dirtreeutil'] ,
     author="Arth Tyagi",
     author_email="arthtyagi7@gmail.com",
     description="A tree utility in Python.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/arthtyagi/dirutil",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU Affero General Public License v3",
         "Operating System :: OS Independent",
     ],
 )