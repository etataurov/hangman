from setuptools import setup, find_packages

setup(
    name='hangman',
    version='',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='',
    license='',
    author='Eugene Tataurov',
    author_email='tatauroff@gmail.com',
    description='',
    entry_points={
        'console_scripts': ['3dhangman = hangman.__main__:main']
    },
    extras_require={
        'dev': ['pytest']
    },
    python_requires=">=3.7"
)
