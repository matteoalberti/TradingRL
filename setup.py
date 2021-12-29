#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="TradingRL",
    description="Library for Automated Trading",
    packages=setuptools.find_packages(exclude=["tests*"]),
)
