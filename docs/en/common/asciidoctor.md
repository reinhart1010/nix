---
layout: page
title: common/asciidoctor (English)
description: "A processor that converts AsciiDoc files to a publishable format."
content_hash: 3a65f20c750dbb24f5ef8ada3067f50cd064ed80
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/asciidoctor.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciidoctor.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/asciidoctor.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/asciidoctor.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciidoctor

A processor that converts AsciiDoc files to a publishable format.
More information: <https://docs.asciidoctor.org>.

- Convert a specific `.adoc` file to HTML (the default output format):

`asciidoctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.adoc</span>

- Convert a specific `.adoc` file to HTML and link a CSS stylesheet:

`asciidoctor -a stylesheet=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/stylesheet.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.adoc</span>

- Convert a specific `.adoc` file to embeddable HTML, removing everything except the body:

`asciidoctor --embedded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.adoc</span>

- Convert a specific `.adoc` file to a PDF using the `asciidoctor-pdf` library:

`asciidoctor --backend=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --require=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asciidoctor-pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.adoc</span>
