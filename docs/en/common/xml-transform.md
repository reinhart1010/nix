---
layout: page
title: common/xml-transform (English)
description: "Transform XML documents using XSLT."
content_hash: 5d5794bb858e1a3892352df37e954533016f6725
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# xml transform

Transform XML documents using XSLT.
More information: <https://xmlstar.sourceforge.net/docs.php>.

- Transform an XML document using an XSL stylesheet, passing one XPATH parameter and one literal string parameter:

`xml transform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/stylesheet.xsl</span>` -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Count='count(/xml/table/rec)'</span>`" -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text="Count="</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Display help:

`xml transform --help`
