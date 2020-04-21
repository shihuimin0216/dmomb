# _*_ coding: utf-8 _*_
import nbformat
from traitlets.config import Config
from nbconvert import HTMLExporter
from html.parser import HTMLParser


class Jupyter_to_html(HTMLParser):
    def to_html(meta):
        # print(meta)
        jake_notebook = nbformat.reads(meta, as_version=4)
        html_exporter = HTMLExporter()
        html_exporter.template_file = 'basic'
        (body, resources) = html_exporter.from_notebook_node(jake_notebook)
        # print("看看resources是什么:", resources.keys())
        print("Resources:", resources.keys())
        print("Metadata:", resources['metadata'].keys())
        print("Inlining:", resources['inlining'].keys())
        print("Extension:", resources['output_extension'])

        print("css:", resources['inlining']['css'])
        print("Metadata:", resources['metadata']['name'])

        html = '<html><head><meta charset="utf-8" /><title>test</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script><style type="text/css">' + \
            resources['inlining']['css'][0] + \
            '</style></head><body>'+body+'</body></html>'
        # html = html.join(resources['inlining']['css'])
        # html = html.join(['< /style ></head>'])
        # html = html.join([body])
        # html = html.join('</html>')
        # print(html)
        return html
