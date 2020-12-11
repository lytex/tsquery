from setuptools import setup, find_packages

setup(
    name='tsquery',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'attrs >= 20',
        'click >= 7',
        'tree_sitter >= 0.2.0',
    ],
    entry_points = {
        'console_scripts': [
            'tsquery = tsquery.__main__:cli'
        ]
    }
)
