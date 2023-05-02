from setuptools import setup


setup(
    name="htpgen",
    version="0.0.1",
    description="Simple lightweight .htpasswd line generator, no Apache required",
    author="Lemon",
    author_email="justlemoncl@gmail.com",
    url="https://github.com/justalemon/htpgen",
    py_modules=[
        "htpgen"
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    python_requires=">=3.8"
)
