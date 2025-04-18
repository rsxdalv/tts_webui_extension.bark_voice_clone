import setuptools

setuptools.setup(
    name="extension_bark_voice_clone",
    packages=setuptools.find_namespace_packages(),
    version="0.0.1",
    author="rsxdalv",
    description="Bark Voice Clone allows cloning voices for use with Bark TTS",
    url="https://github.com/rsxdalv/extension_bark_voice_clone",
    project_urls={},
    scripts=[],
    install_requires=[
        "bark_hubert_quantizer @ https://github.com/rsxdalv/bark-voice-cloning-HuBERT-quantizer/releases/download/v0.0.5/bark_hubert_quantizer-0.0.5-py3-none-any.whl",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
