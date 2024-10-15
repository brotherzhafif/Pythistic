from setuptools import setup, find_packages

setup(
    name='Pythistic',
    version='1.1.1',
    description='A Python library for statistical data processing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='BrotherZhafif',
    author_email='bangz1504@gmail.com',
    url='https://github.com/brotherzhafif/Pythistic',  # Ganti dengan URL repository GitHub kamu
    license='MIT',
    packages=find_packages(),
    install_requires=[
    'matplotlib',
    'matplotlib-venn',
    'numpy',
    'tabulate',
    'pandas',
    'scipy',],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
