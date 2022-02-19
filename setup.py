from setuptools import setup

setup(
    name="bkmk",
    version=4.0,
    author="mclds",
    author_email="mclds@protonmail.com",
    description="TUI app for bookmarking.",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://codeberg.org/micaldas/bkmk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["bkmk"],
    install_requires=[
        "click",
        "colr",
        "mysql.connector",
        "future",
        "questionary",
        "fire",
        "icecream",
    ],
    include_package_data=True,
)
