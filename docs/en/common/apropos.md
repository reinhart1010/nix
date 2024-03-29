---
layout: page
title: common/apropos (English)
description: "Search the manual pages for names and descriptions."
content_hash: f632fd1f794dc3b0e9ee0ccddfdaf0b5d2e8fa3c
last_modified_at: 2024-02-09
related_topics:
  - title: Deutsch version
    url: /de/common/apropos.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/apropos.html
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
tldri18n_status: 2
---
# apropos

Search the manual pages for names and descriptions.
More information: <https://manned.org/apropos>.

- Search for a keyword using a regular expression:

`apropos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Search without restricting the output to the terminal width ([l]ong output):

`apropos -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Search for pages that match [a]ll the expressions given:

`apropos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression_1</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression_2</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression_3</span>
