---
layout: page
title: common/daps (English)
description: "DAPS is an open source program for transforming DocBook XML into output formats such as HTML or PDF."
content_hash: 4934fe1d9d2d7a5ac7514d60627ddb0f958cfab9
---
# daps

DAPS is an open source program for transforming DocBook XML into output formats such as HTML or PDF.
More information: <https://opensuse.github.io/daps/doc/index.html>.

- Check if a DocBook XML file is valid:

`daps -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xml</span>` validate`

- Convert a DocBook XML file into PDF:

`daps -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xml</span>` pdf`

- Convert a DocBook XML file into a single HTML file:

`daps -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xml</span>` html --single`

- Display help:

`daps --help`

- Display version:

`daps --version`
