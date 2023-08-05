from setuptools import setup, find_packages


def requirements_from_file(file_name):
    return open(file_name).read().splitlines()


setup(
    name="llm-eval",
    version="0.1.0",
    url='https://github.com/kz-000/llm-eval',
    install_requires=requirements_from_file('requirements.txt'),
    packages=find_packages("llmeval"),
    package_dir={'', 'llmeval'}
)
