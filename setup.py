#!/usr/bin/env python

import os
import sys

from setuptools import find_packages, setup

exec(open("colorfield/version.py").read())

package_name = "django-colorfield"
package_url = f"https://github.com/fabiocaccamo/{package_name}"
package_path = os.path.abspath(os.path.dirname(__file__))
download_url = f"{package_url}/archive/{__version__}.tar.gz"
documentation_url = f"{package_url}#readme"
issues_url = f"{package_url}/issues"
sponsor_url = "https://github.com/sponsors/fabiocaccamo/"
twitter_url = "https://twitter.com/fabiocaccamo"

long_description_file_path = os.path.join(package_path, "README.md")
long_description_content_type = "text/markdown"
long_description = ""
try:
    with open(long_description_file_path, "r", encoding="utf-8") as f:
        long_description = f.read()
except IOError:
    pass

setup(
    name=package_name,
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    include_package_data=True,
    version=__version__,
    description="simple color field for your models with a nice color-picker in the admin-interface.",
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    author="Jared Forsyth, Fabio Caccamo",
    author_email="jared@jaredforsyth.com, fabio.caccamo@gmail.com",
    url=package_url,
    download_url=download_url,
    project_urls={
        "Documentation": documentation_url,
        "Issues": issues_url,
        "Funding": sponsor_url,
        "Twitter": twitter_url,
    },
    keywords=[
        "django",
        "colorfield",
        "colorpicker",
        "color",
        "field",
        "picker",
        "chooser",
        "admin",
        "python",
    ],
    requires=[
        "django (>= 2.2)",
    ],
    install_requires=[
        "Pillow (>= 9.0.0)",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Build Tools",
    ],
)
