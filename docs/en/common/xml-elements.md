---
layout: page
title: common/xml-elements (English)
description: "Extract elements and display the structure of an XML document."
content_hash: 4ca0f61d1396f62e3d3b4f28306c26c6e12649a8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xml elements

Extract elements and display the structure of an XML document.
More information: <http://xmlstar.sourceforge.net/docs.php>.

- Extract elements from an XML document (producing XPATH expressions):

`xml elements `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/elements.xpath</span>

- Extract elements and their attributes from an XML document:

`xml elements -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/elements.xpath</span>

- Extract elements and their attributes and values from an XML document:

`xml elements -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/elements.xpath</span>

- Print sorted unique elements from an XML document to see its structure:

`xml elements -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Print sorted unique elements from an XML document up to a depth of 3:

`xml elements -d`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Display help for the `elements` subcommand:

`xml elements --help`
