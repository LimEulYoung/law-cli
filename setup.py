from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="lawcli",
    version="0.1.0",
    description="AI-powered legal document search CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LimEulYoung/law-cli",
    author="LimEulYoung",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Legal Industry",
        "Topic :: Text Processing :: General",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="law legal search cli korean",
    packages=find_packages(),
    python_requires=">=3.8, <4",
    install_requires=[],
    extras_require={
        "dev": ["pytest", "black", "flake8"],
    },
    entry_points={
        "console_scripts": [
            "lawcli=lawcli.cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/LimEulYoung/law-cli/issues",
        "Source": "https://github.com/LimEulYoung/law-cli",
    },
)