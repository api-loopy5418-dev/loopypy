from setuptools import setup, find_packages

setup(
    name="loopypy",
    version="0.0.1",
    author="loopy5418.dev",
    author_email="admin@loopy5418.dev",
    description="The official python wrapper for api.loopy5418.dev",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/api-loopy5418-dev/loopypy",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
