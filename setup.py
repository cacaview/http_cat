from setuptools import setup

setup(
    name="http_cat",
    version="0.1",
    author="cacaview",
    author_email="cacaview@foxmail.com",
    description="A simple httpcat call function returns image data when called",
    license="MIT",
    packages=["http_cat"],
    install_requires=["requests"],
    url="https://github.com/cacaview/http_cat",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
