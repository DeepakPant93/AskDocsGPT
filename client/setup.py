from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="ask-docs-client",  # Name of your package
    version="0.1.0",  # Version of your package
    packages=find_packages(),  # Automatically find your package
    include_package_data=True,  # Include additional files specified in MANIFEST.in
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Proprietary",
        "Operating System :: OS Independent",
    ],
    install_requires=required,  # Read the dependencies from requirements.txt
    python_requires=">=3.10",
)
