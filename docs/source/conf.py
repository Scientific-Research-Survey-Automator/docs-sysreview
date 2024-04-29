# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SysReview'
copyright = '2024, Binghamton University'
author = 'Rishank'

release = '1.0'
version = release

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_logo = 'images/logos/smallLogo.png'
html_favicon = 'images/logos/favicon.png'
html_title = 'Systematic Review'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'navigation_depth': -1,
    'collapse_navigation': False,
    'prev_next_buttons_location': 'both'
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]
