from setuptools import setup, find_packages

setup(
    name="physical-security-event-summarizer",
    version="0.1.0",
    description="Ingest, summarize, and classify physical security incidents.",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
        "pydantic",
        "pytest",
        "requests",
        "langdetect",
        "ruff"
    ],
    include_package_data=True,
    python_requires=">=3.9",
)
