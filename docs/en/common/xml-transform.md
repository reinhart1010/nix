---
layout: page
title: common/xml-transform (English)
description: "Transform XML documents using XSLT."
content_hash: 367f9b10fbc8cd8f98b38ba7fdf03ef328e4093f
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# xml transform

Transform XML documents using XSLT.
More information: <http://xmlstar.sourceforge.net/docs.php>.

- Transform an XML document using an XSL stylesheet, passing one XPATH parameter and one literal string parameter:

`xml transform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/stylesheet.xsl</span>` -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Count='count(/xml/table/rec)'</span>`" -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text="Count="</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Display help:

`xml transform --help`
