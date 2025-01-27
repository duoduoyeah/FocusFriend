from setuptools import setup, find_packages

setup(
    name="focus-friend",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tqdm>=4.65.0",
    ],
    entry_points={
        'console_scripts': [
            'focus-friend=focus_friend.app.main:main',
        ],
    },
    author="Duoduoyuan",
    author_email="",
    description="A focus tool for people with ADHD",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)