from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author="Craig Dalrymple",
    author_email="craig.dalrymple91@gmail.com",
    description="Webotron 80 is a tool to manage deploying S3 static websites. Created during Robin Norwood's Python course on acloudguru",
    license="GPLv3+",
    packages=['webotron'],
    url="https://github.com/craig-python/automating-aws-with-python/01-webotron",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    ''',
)
