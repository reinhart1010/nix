---
layout: page
title: common/xml-elements (English)
description: "Extract elements and display the structure of an XML document."
content_hash: 2ee9111b0fbc502d40720d3b1160ee8306a06db3
last_modified_at: 2024-01-30
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

- Display help:

`xml elements --help`
