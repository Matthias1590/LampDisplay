from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="lamp_display",
    packages=["lamp_display"],
    version="1.1",
    license="MIT",
    description="A Python module to simulate a Minecraft lamp display.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Matthias Wijnsma",
    author_email="matthias.wijnsma@outlook.com",
    url="https://github.com/Matthias1590/LampDisplay",
    download_url="https://github.com/Matthias1590/LampDisplay/archive/refs/tags/v1.1.tar.gz",
    python_requires=">=3.6",
    install_requires=[
        "pygame",
    ],
)
