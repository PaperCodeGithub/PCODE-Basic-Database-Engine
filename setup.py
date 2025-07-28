from setuptools import setup, find_packages

setup(
    name='paperbase',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    author='PaperCode',
    author_email='aritra.paper.code@gmail.com',
    description='Simple file-based database with user auth',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)
