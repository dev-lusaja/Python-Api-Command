import api
from pip.req import parse_requirements
from setuptools import setup, find_packages
long_description = open('README.md').read()
requires = parse_requirements('requirements.txt', session=False)
install_requires = [str(r.req) for r in requires]
setup(
    name                = "ApiCommand",
    description         = "Api command",
    packages            = find_packages(),
    author              = "Oscar Sanchez",
    author_email        = "janoone52@gmail.com",
    scripts             = ["bin/api"],
    install_requires    = install_requires,
    version             = api.__version__,
    url                 = "https://github.com/dev-lusaja/Python-Api-Command.git",
    license             = "MIT",
    zip_safe            = False,
    keywords            = "project, manager, api",
    long_description    = long_description,
    classifiers      = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ]
)