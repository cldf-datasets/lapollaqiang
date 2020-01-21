from setuptools import setup


setup(
    name='cldfbench_lapollaqiang',
    py_modules=['cldfbench_lapollaqiang'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'lapollaqiang=cldfbench_lapollaqiang:Dataset',
        ],
        'cldfbench.commands': [
            'lapollaqiang=commands',
        ],
    },
    install_requires=[
        'cldfbench',
        'pyglottolog',
        'pyconcepticon',
        'pyclts',
        'segments',
        'lingpy',
        'pyigt',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
