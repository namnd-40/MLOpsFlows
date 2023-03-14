"""The setup module"""
from pathlib import Path

from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), encoding="UTF-8") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

test_packages = [
    "pytest==7.1.2",
    "pytest-cov==4.0.0",
    "pytest-html-reporter==0.2.9",
]

style_packages = [
    "black==22.6.0",
    "flake8==4.0.1",
    "isort==5.9.3",
    "pre-commit==2.19.0",
]

docs_packages = [
    "mkdocs==1.1.2",
    "mkdocs-macros-plugin==0.5.0",
    "mkdocs-material==6.2.4",
    "mkdocstrings==0.14.0",
]
# Define our package
setup(
    name="mlopsflows",
    version=0.1,
    description="MLOpsFlows projects.",
    author="500ae",
    author_email="500ae@gmail.com",
    url="https://mlopsflows.com/",
    python_requires=">=3.8",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
    extras_require={
        "dev": docs_packages + style_packages + test_packages,
        "docs": docs_packages,
        "test": test_packages,
    },
)
