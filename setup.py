from setuptools import setup, find_packages

setup(
    name='movie-kiss',
    version='0.1.0',
    description='A movie recommendation system',
    author='Alexandre Leroux',
    author_email='alex.leroux89@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)