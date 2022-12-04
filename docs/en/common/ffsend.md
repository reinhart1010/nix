---
layout: page
title: common/ffsend (English)
description: "Easily and securely share files from command-line."
content_hash: ace551c072b3b148570bacb66b526c81ad6f5e35
last_modified_at: 2022-12-04
related_topics:
  - title: Deutsch version
    url: /de/common/ffsend.html
    icon: bi bi-globe
---
# ffsend

Easily and securely share files from command-line.
More information: <https://gitlab.com/timvisee/ffsend>.

- Upload a file:

`ffsend upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Download a file:

`ffsend download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Upload a file with password:

`ffsend upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Download a file protected by password:

`ffsend download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Upload a file and allow 4 downloads:

`ffsend upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>
