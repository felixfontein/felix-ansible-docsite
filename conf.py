# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import datetime

year = datetime.date.today().year

# -- Project information -----------------------------------------------------

project = 'Ansible collections'
copyright = f'2020—{year}, Felix Fontein'
author = 'Felix Fontein'
version = ''

html_short_title = 'Ansible Collections Documentation'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx_antsibull_ext', 'notfound.extension']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []



# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'ansible'

highlight_language = 'YAML+Jinja'

# Substitutions, variables, entities, & shortcuts for text which do not need to link to anything.
# For titles which should be a link, use the intersphinx anchors set at the index, chapter, and section levels, such as  qi_start_:
# |br| is useful for formatting fields inside of tables
# |_| is a nonbreaking space; similarly useful inside of tables
rst_epilog = """
.. |br| raw:: html

   <br>
.. |_| unicode:: 0xA0
    :trim:
"""


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_show_sphinx = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

display_version = False

html_theme_options = {
}

html_css_files = [
    'ansible.css',
]

html_use_smartypants = True
html_use_modindex = False
html_use_index = False
html_copy_source = False

# Note:  Our strategy for intersphinx mappings is to have the upstream build location as the
# canonical source and then cached copies of the mapping stored locally in case someone is building
# when disconnected from the internet.  We then have a script to update the cached copies.
#
# Because of that, each entry in this mapping should have this format:
#   name: ('http://UPSTREAM_URL', (None, 'path/to/local/cache.inv'))
#
# The update script depends on this format so deviating from this (for instance, adding a third
# location for the mappning to live) will confuse it.
intersphinx_mapping = {
    'python': ('https://docs.python.org/2/', (None, '../python2.inv')),
    'python3': ('https://docs.python.org/3/', (None, '../python3.inv')),
    'jinja2': ('http://jinja.palletsprojects.com/', (None, '../jinja2.inv')),
    'ansible_devel': ('https://docs.ansible.com/ansible/devel/', (None, '../ansible_devel.inv')),
}

# linckchecker settings
linkcheck_ignore = [
    r'http://irc\.freenode\.net',
]
linkcheck_workers = 25
# linkcheck_anchors = False
