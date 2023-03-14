"""The setup module
"""
from pathlib import Path

from setuptools import find_namespace_packages, setup

BASE_DIR = Path(__file__).parent

# Load packages from requirements.txt
with open(Path(BASE_DIR, "requirements.txt"), encoding='UTF-8') as file:
    required_packages = [ln.strip() for ln in file.readlines()]

test_packages = [
    "great-expectations==0.13.14",
    "pytest==6.0.2",
    "pytest-cov==2.10.1",
    "pytest-html-reporter==0.2.9",
]

dev_packages = [
    "black==20.8b1",
    "flake8==3.8.3",
    "isort==5.5.3",
    "jupyterlab==2.2.8",
    "pre-commit==2.11.1",
]

docs_packages = [
    "mkdocs=1.3.0",
    "mkdocs-material=8.2.15",
    "mkdocs-macros-plugin==0.5.0",
    "mkdocstrings==0.14.0",
]

setup(
    name="MLOpsFlows",
    version="0.1",
    license="None",
    description="Implementation of MLOps Flows",
    author="500ae",
    author_email="500ae",
    url="https://github.com/namnd00/MLOpsFlows",
    keywords=[
        "machine-learning",
        "artificial-intelligence",
        "mlops",
    ],
    python_requires=">=3.8.10",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
    extras_require={
        "test": test_packages,
        "dev": dev_packages,
        "docs": docs_packages,
    },
)
