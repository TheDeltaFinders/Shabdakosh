#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2019-09-11 22:07

import setuptools

with open("README.md",'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="shabdakosh",
    version="0.0.1",
    author="Prakash Gautam",
    author_email="info@pgautam.com.np",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url='https://github.com/thedeltafinders/shabdakosh',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License ::OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['bin/shabdakosh']
)

