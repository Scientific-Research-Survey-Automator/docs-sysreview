# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SysReview'
copyright = '2024, Binghamton University'
author = "Rishank Karkera, Tarun Parmar"

def get_author_for_latex(author_names: str):
    latex_line_break = "\\\\"
    return (author_names
            .replace(", ", latex_line_break)
            .replace(",", latex_line_break))


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).

latex_documents = [
    ('index', f'{project.lower()}.tex', project, get_author_for_latex(author), 'manual'),
]

release = '1.0'
version = release

youtube_video_link = 'https://player.vimeo.com/video/940944648'
rst_epilog = """
.. role:: raw-html(raw)
   :format: html
.. |tutorial_video_link| replace:: {link}
.. |tutorial_frame_link| replace:: :raw-html:`<iframe src="{link}" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>`
""".format(link=youtube_video_link)

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.jquery'
]
autosectionlabel_prefix_document = True

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

html_js_files = [
    'js/custom.js'
]
