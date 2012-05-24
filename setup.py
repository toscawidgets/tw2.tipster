from setuptools import setup, find_packages

setup(
    name='tw2.tipster',
    version='2.0b9',
    description='Tips for your website :)',
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    license='MIT',
    url='http://github.com/toscawidgets/tw2.tipster',
    install_requires=[
        "tw2.jqplugins.ui",
        "mako"
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    tests_require = [
        'nose',
        'BeautifulSoup',
        'Genshi',
        'mako',
        # formencode isn't actually needed, but is just here to patch up
        # tw2.forms
        'formencode',
        'strainer',
    ],
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.tipster
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
