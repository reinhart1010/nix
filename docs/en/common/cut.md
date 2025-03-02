---
layout: page
title: common/cut (English)
description: "Cut out fields from `stdin` or files."
content_hash: 74f86ef25e9578a86d4d723b8a6368dd50a17a83
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/common/cut.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/cut.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cut.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cut.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cut.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cut.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cut.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cut.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cut

Cut out fields from `stdin` or files.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html>.

- Print a specific [c]haracter/[f]ield range of each line:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | cut --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">characters|fields</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- Print a [f]ield range of each line with a specific [d]elimiter:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | cut --delimiter "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delimiter</span>`" --fields `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- Print a [c]haracter range of each line of the specific file:

`cut --characters `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print specific [f]ields of `NUL` terminated lines (e.g. as in `find . -print0`) instead of newlines:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | cut --zero-terminated --fields `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
