#######################
pelican-metadataparsing
#######################

A plugin for `Pelican
<http://pelican.readthedocs.org/en/latest/>`_ that
allows the easy definition of custom metadata parsers.


Install
=======

To install the library, you can use
`pip
<http://www.pip-installer.org/en/latest/>`_

.. code-block:: bash

    $ pip install pelican-metadataparsing


Usage
=====

1. Update ``pelicanconf.py``:

   1. Add ``metadataparsing`` to ``PLUGINS``.
      
      You should add it before any metadata-affecting plugins.

      .. code-block:: python
      
          PLUGINS = [..., 'metadataparsing', ...]

   2. Define your custom metadata parsers through the ``METADATA_PARSERS``
      setting:

      .. code-block:: python

          METADATA_PARSERS = {
              "<metadata-field-name1>": <function parser1(x)>,
              "<metadata-field-name2>": <function parser2(x)>
          }

2. Corresponding fields of the ``page``, ``article`` or ``entity``
   object will have the value returned from the respective parser
   function.


Example
=======

Gallery Metadata
----------------

``pelicanconf.py``:

.. code-block:: python

    import collections
    import six

    GalleryItem = collections.namedtuple("GalleryItem", ["url", "description"])
    def parse_gallery(string):
        if string is None or not isinstance(string, collections.Iterable):
            return None

        if not isinstance(string, six.string_types):
            string = '\n'.join(string)

        items = []

        for line in string.split('\n'):
            if not line:
                continue

            parts = line.split("||")

            url = parts[0].strip()

            if len(parts) == 1:
                description = None
            else:
                description = parts[1].strip()

            items.append(GalleryItem(url, description))

        return items

    METADATA_PARSERS = {
        "Gallery": parse_gallery
    }

Theme:

.. code-block:: html

    {% if article.gallery %}
    <div class="article-gallery">
        <h3>Gallery:</h3>
        <ul>
            {% for image in article.gallery %}
            <li>{{ colorbox(image.url, image.description) }}</li>
            {% endfor %}
        </ul>
    </div>
    {% endif %}


Multi-line metadata to simple string
------------------------------------
.. code-block:: python

    import collections
    import six

    def parse_description(string):
        if string is None or isinstance(string, six.string_types):
            return string

        if isinstance(string, collections.Iterable):
            string = " ".join(string)

        return string


    METADATA_PARSERS = {
        "Description": parse_description
    }



For a working example check `my site
<http://www.alexjf.net>`_ and `my site's source code
<https://github.com/AlexJF/alexjf.net>`_.

