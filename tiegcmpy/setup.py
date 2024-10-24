from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='tiegcmpy',
    version='2.1.0',
    author = "Nikhil Rao",
    author_email = "nikhilr@ucacd r.edu",
    description='A Python3 post processing tool for TIE-GCM',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/NCAR/tiegcmpy', 
    python_requires='>=3.8',
    install_requires=[
        'cartopy',
        'matplotlib',
        'numpy',
        'xarray',
        'ipython',
        'geomag',
    ],
    package_dir={'': 'src'},  
    packages=find_packages(where='src'), 
    entry_points={
        'console_scripts': [
            'lat_lon= tiegcmpy.cmd.cmd_lat_lon:cmd_plt_lat_lon',
            'lev_var= tiegcmpy.cmd.cmd_lev_var:cmd_plt_lev_var',
            'lev_lat= tiegcmpy.cmd.cmd_lev_lat:cmd_plt_lev_lat',
            'lev_lon= tiegcmpy.cmd.cmd_lev_lon:cmd_plt_lev_lon',
            'lev_time= tiegcmpy.cmd.cmd_lev_time:cmd_plt_lev_time',
            'lat_time= tiegcmpy.cmd.cmd_lat_time:cmd_plt_lat_time',
            
        ]
    }
)
