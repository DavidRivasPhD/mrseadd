# pylint: disable = C0111
from setuptools import find_packages, setup

with open("README.md", "r") as f:
    DESCRIPTION = f.read()

setup(name="mrse",
      version="1.2.0",
      author="Blockchain Guru",
      description="AI-powered literature discovery and review engine for medical/scientific papers",
      long_description=DESCRIPTION,
      long_description_content_type="text/markdown",
      url="https://github.com/DavidRivasPhD/mrse",
      project_urls={
          "Documentation": "https://github.com/DavidRivasPhD/mrse",
          "Issue Tracker": "https://github.com/DavidRivasPhD/mrse/issues",
          "Source Code": "https://github.com/DavidRivasPhD/mrse",
      },
      license="Apache 2.0: http://www.apache.org/licenses/LICENSE-2.0",
      packages=find_packages(),
      # packages=["src"],
      # package_dir={"src": "src"},
      keywords="search embedding machine-learning nlp medical scientific papers",
      python_requires=">=3.6",
      entry_points={
          "console_scripts": [
              "mrse-search = src.__main__:main",
          ],
      },
      install_requires=[
          "biopython>=1.78",
          "numpy>=1.19.2",
      ],
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Topic :: Scientific/Engineering :: Artificial Intelligence",
          "Topic :: Software Development",
          "Topic :: Text Processing :: Indexing",
          "Topic :: Utilities"
      ])
