from setuptools import setup, find_packages

setup(
    name="life_expectancy_analysis",                  # Tên package
    version="0.1.0",                     # Phiên bản của package
    author="ethan Nguyen",                  # Tác giả
    author_email="nguyentanhoang1808@gmail.com",  # Email của tác giả
    description="A short description",   # Mô tả ngắn gọn về dự án
    long_description=open("README.md").read(),  # Mô tả chi tiết từ README.md
    long_description_content_type="text/markdown",  # Định dạng (markdown)
    url="https://github.com/tanhoang1808/Life_expectancy_analysis",  # Link tới repository
    packages=find_packages(),            # Tự động tìm kiếm các package con
    install_requires=[
        "numpy>=1.21.0",                 # Dependency (yêu cầu thư viện)
        "pandas>=1.3.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",   # Phiên bản Python hỗ trợ
        "License :: OSI Approved :: MIT License", # Loại license
        "Operating System :: OS Independent",    # Hệ điều hành hỗ trợ
    ],
    python_requires='>=3.7',             # Phiên bản Python tối thiểu
)
