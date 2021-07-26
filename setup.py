from setuptools import setup

if __name__ == '__main__':

    long_description = open('README.md').read()

    setup(
        name='oui-search',
        version='1.0',
        description='This simple CLI tool does OUI lookups using Wireshark\'s Gitlab Repo as the source.',
        author='Josias Alvarado',
        author_email='josiasjag@gmail.com',
        url='https://github.com/pointerish/oui',
        packages=[
            'oui-lookup',
            ],
        long_description=long_description,
        license='MIT',
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Operating System :: OS Independent',
            'Topic :: Software Development',
            'Topic :: System :: Networking',
            'Intended Audience :: Developers',
            'Development Status :: 3 - Alpha',
            ],
        )