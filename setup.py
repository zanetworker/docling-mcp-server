from setuptools import setup, find_packages

setup(
    name="mcp-docling",
    version="0.1.0",
    description="MCP Server for Docling document conversion",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "docling",
        "mcp[cli]>=1.2.0",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "mcp-docling=mcp_docling:main",
        ],
    },
) 