---
layout: page
title: common/daps (English)
description: "An open source program for transforming DocBook XML into output formats such as HTML or PDF."
content_hash: f0d4d02d91abe14627286692b59c47c0cd2cd0d0
last_modified_at: 2023-11-15
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/daps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# daps

An open source program for transforming DocBook XML into output formats such as HTML or PDF.
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
