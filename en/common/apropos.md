---
layout: page
title: common/apropos (English)
description: "Search the manual pages for names and descriptions."
content_hash: 1bc5a43eba28d76d59dd5b486d3311e70f840ff5
related_topics:
  - title: Deutsch version
    url: /de/common/apropos.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/apropos.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/apropos.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/apropos.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/apropos.html
    icon: bi bi-globe
---
# apropos

Search the manual pages for names and descriptions.
More information: <https://manned.org/apropos>.

- Search for a keyword using a regular expression:

`apropos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Search without restricting the output to the terminal width:

`apropos -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Search for pages that contain all the expressions given:

`apropos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression_1</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression_2</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression_3</span>
