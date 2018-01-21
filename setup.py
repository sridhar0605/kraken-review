from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
    long_description = long_description.replace('\r', '')
except (ImportError, OSError):
    import io
    with io.open('README.md', encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='kraken_plot',
    packages=['kraken_plot'],
    version='0.0.1',
    description='Plot the summary output from Kraken.',
    long_description=long_description,
    author='clintval',
    author_email='valentine.clint@gmail.com',
    url='https://github.com/clintval/kraken-plot',
    download_url='https://github.com/clintval/kraken-plot/archive/v0.0.1.tar.gz',  # noqa
    py_modules=['kraken_plot'],
    install_requires=[
        'ete3',
        'numpy',
        'toytree',
    ],
    extras_require={
        'test': ['nose'],
        'fancytest': ['nose', 'nose-progressive', 'coverage'],
    },
    scripts=[],
    license='MIT',
    zip_safe=True,
    keywords='kraken tree phylogeny taxonomy classification',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3.6',
    ]
)
