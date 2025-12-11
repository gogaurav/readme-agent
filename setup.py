from setuptools import setup, find_packages

setup(
    name="readme-agent",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "readme-agent = agent_main:main",  # maps CLI command → Python function
        ],
    },
)
