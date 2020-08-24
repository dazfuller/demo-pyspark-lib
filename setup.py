from setuptools import setup

setup(
    name="dazspark",
    version="0.2",
    description="A demo PySpark library",
    url="https://github.com/dazfuller/demo-pyspark-lib",
    author="dazfuller",
    author_email="daz.fuller@gmail.com",
    packages=[
        "dazspark"
    ],
    install_requires=[
        "pyspark==3.0.0",
        "pandas==1.1.0",
        "pyarrow==1.0.0"
    ],
    zip_safe=False
)
