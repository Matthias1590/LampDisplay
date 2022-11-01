from setuptools import setup

setup(
    name="lamp_display",
    packages=["lamp_display"],
    version="1.0",
    license="MIT",
    description="A Python module to simulate a Minecraft lamp display.",
    author="Matthias Wijnsma",
    author_email="matthias.wijnsma@outlook.com",
    url="https://github.com/Matthias1590/LampDisplay",
    download_url="https://github.com/Matthias1590/LampDisplay/archive/refs/tags/v1.0.tar.gz",
    python_requires=">=3.6",
    install_requires=[
        "pygame",
    ],
)
