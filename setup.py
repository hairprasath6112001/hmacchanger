import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Here is the module name.
    name="hmacchanger",
 
    #version of the module
    version="1.2",
 
    #Name of Author
    author="HariPrasath.S.S",
    
    #Path of Script
    scripts=["hmacchanger/hmacchanger"],
 
    #your Email address
    author_email="hariprasath6112001@gmail.com",
 
    #Small Description about module
    description="Changing MAC Address",
 
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
 
    #Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/hairprasath6112001/hmacchanger-v1.2",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
