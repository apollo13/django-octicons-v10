from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="django-octicons-v10",
    packages=find_packages(exclude=("tests",)),
    package_data={"octicons_v10": ["templatetags/octicons.json", "templatetags/keywords.json"]},
    version="3.0.1",
    license="MIT",
    description="Django templatetags for GitHub Octicons v10.0.0+.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Jay Newey',
    author_email="jay.newey01@gmail.com",
    url="https://github.com/jaynewey/django-octicons-v10",
    download_url="https://github.com/jaynewey/django-octicons-v10/archive/v3.0.1.tar.gz",
    keywords=["octicons", "django", "templatetags"],
    install_requires=[
        "Django>=2.0.0,<4.0.0",
    ],

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django",
    ],
)
