from setuptools import setup, find_packages

setup(
    name="InterVelo",
    version="0.1.1",
    author="YurouWang",
    author_email="rapunzel@sjtu.edu.cn",
    description="A deep learning framework to simutaneously learn the pseudotime and RNA velocity.",
    long_description=open("README.md").read(), 
    long_description_content_type="text/markdown",
    url="https://github.com/yurouwang-rosie/InterVelo",
    packages=find_packages(), 
    install_requires=[
        "numpy", 
        "scvelo",
        "anndata",
	"torch",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  
    entry_points={
        "console_scripts": [
            "InterVelo=InterVelo.main:main",  # 创建命令行工具
        ],
    },
)
