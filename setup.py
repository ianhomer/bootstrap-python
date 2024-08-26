from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="foo",
    version="0.0.1",
    description="Foo",
    packages=["foo"],
    entry_points={
        "console_scripts": [
            "bootstrap_python_foo=foo.cli.foo:run",
        ]
    },
    install_requires=required
)
