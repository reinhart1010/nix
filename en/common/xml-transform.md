---
layout: page
title: common/xml-transform (English)
description: "Transform XML documents using XSLT."
content_hash: 07091600739acd9bf5ed64fd206c80d29ee74144
---
# xml transform

Transform XML documents using XSLT.
More information: <http://xmlstar.sourceforge.net/docs.php>.

- Transform an XML document using an XSL stylesheet, passing one XPATH parameter and one literal string parameter:

`xml transform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/stylesheet.xsl</span>` -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Count='count(/xml/table/rec)'</span>`" -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text="Count="</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Display help for the `transform` subcommand:

`xml transform --help`
