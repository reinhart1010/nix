---
layout: page
title: osx/xsltproc (English)
description: "Transform XML with XSLT to produce output (usually HTML or XML)."
content_hash: c4521a9575f8bdba0b9c09a10977a3878d47851f
related_topics:
  - title: 中文 version
    url: /zh/osx/xsltproc.html
    icon: bi bi-globe
---
# xsltproc

Transform XML with XSLT to produce output (usually HTML or XML).
More information: <http://www.xmlsoft.org/xslt/xsltproc.html>.

- Transform an XML file with a specific XSLT stylesheet:

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stylesheet.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xmlfile.xml</span>

- Pass a value to a parameter in the stylesheet:

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.html</span>` --stringparam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stylesheet.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xmlfile.xml</span>
