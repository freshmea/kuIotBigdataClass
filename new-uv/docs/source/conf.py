import os
import sys

# 프로젝트의 루트 디렉토리 경로 추가
sys.path.insert(0, os.path.abspath('../../src'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'new-uv'
copyright = '2025, choi'
author = 'choi'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',        # Docstring 기반 자동 문서화
    'sphinx.ext.napoleon',       # Google/NumPy 스타일 docstring 지원
    'sphinx.ext.viewcode',       # 소스 코드 링크 추가
]
extensions.append('myst_parser')
templates_path = ['_templates']
exclude_patterns = []

language = 'ko'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' # 테마설정
html_static_path = ['_static']
