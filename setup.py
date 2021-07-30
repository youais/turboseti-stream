import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "turboseti_stream-youais",
    version = "0.0.1",
    author = "Yiwei Chai, Wael Farah, Luigi Cruz, Richard Elkins",
    author_email = "mychai@sas.upenn.edu",
    description = "An adapted turboSETI FindDoppler function for analysing data stored in RAM.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/luigifcruz/turboseti-stream.git",
    project_urls = {
        "Issues": "https://github.com/luigifcruz/turboseti-stream/issues",
    }
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src"),
    python_requires=">=3.6",
)
