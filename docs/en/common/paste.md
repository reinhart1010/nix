---
layout: page
title: common/paste (English)
description: "Merge lines of files."
content_hash: ed5ec31d600e807fde74d813f1152811583e7c33
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/paste.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/paste.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/paste.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paste

Merge lines of files.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/paste-invocation.html>.

- Join all the lines into a single line, using TAB as delimiter:

`paste -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Join all the lines into a single line, using the specified delimiter:

`paste -s -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delimiter</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Merge two files side by side, each in its column, using TAB as delimiter:

`paste `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Merge two files side by side, each in its column, using the specified delimiter:

`paste -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delimiter</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Merge two files, with lines added alternatively:

`paste -d '\n' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>
