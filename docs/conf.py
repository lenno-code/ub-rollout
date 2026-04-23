import os
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'UC Rollout Customer'
copyright = '2026, Lennard Rhenisch'
author = 'Lennard Rhenisch'
release = '0.1.0'

# -- General configuration -----------------------------------------
extensions = [
    'sphinx_needs',  # Requirements management
    'sphinxcontrib.plantuml',  # PlantUML support
    'sphinx.ext.graphviz',     # Graphviz fallback (optional)
]

# -- PlantUML configuration ----------------------------------------
# Path to PlantUML JAR (relative to conf.py location)
plantuml = f'java -jar {os.path.join(os.path.dirname(__file__), "utils", "plantuml.jar")}'

# Output format: 'svg' recommended for quality and scalability
plantuml_output_format = 'svg'

# Show syntax errors as images (helpful for debugging)
plantuml_syntax_error_image = True

needs_flow_engine = "plantuml"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Sphinx-Needs configuration ------------------------------------
# Load configuration from external TOML file
# This is the key line that connects sphinx-needs to ubproject.toml
needs_from_toml = "ubproject.toml"

# -- Options for HTML output ---------------------------------------
html_theme = 'furo'
html_static_path = ['_static']
