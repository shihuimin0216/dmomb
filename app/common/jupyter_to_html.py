# _*_ coding: utf-8 _*_
import nbformat
from traitlets.config import Config
from nbconvert import HTMLExporter


class Jupyter_to_html:
    def to_html(meta):
        print(meta)
        jake_notebook = nbformat.reads(meta, as_version=4)
        html_exporter = HTMLExporter()
        html_exporter.template_file = 'basic'
        (body, resources) = html_exporter.from_notebook_node(jake_notebook)
        return body
