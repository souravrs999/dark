from setuptools import setup


def _get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements


setup(
    name='speechemotionrecognition',
    version='1.0',
    packages=['speechemotionrecognition'],
    url='https://github.com/souravrs999/dark/tree/master/speech_emotion_recognition',
    license='MIT',
    install_requires=_get_requirements(),
    author='Sourav R S',
    author_email='souravraveendran6@@gmail.com',
    description='Tool to perform speech emotion recognition'
)
