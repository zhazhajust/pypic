from setuptools import setup, find_packages  
  
setup(  
    name = "pypic",  
    version = "0.0.1",
    keywords = ("pic data reader"),  
    description = "eds sdk",  
    long_description = "eds sdk for python",  
    license = "MIT Licence",

    url = "http://github.com",  
    author = "Jie.Cai",  
    author_email = "jiecai@stu.pku.edu.com",  
    
    packages = find_packages(),  
    include_package_data = True,  
    platforms = "any",  
    install_requires = ["numpy", "numba", "lasy"],  
  
    scripts = [],  
    entry_points = {  
        'console_scripts': [  
            'test = test.help:main'  
        ]  
    }  
)
