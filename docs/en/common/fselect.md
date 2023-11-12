---
layout: page
title: common/fselect (English)
description: "Find files with SQL-like queries."
content_hash: cd85fc41cd2b04e4bbf186e03f85f02e88e1cc4d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# fselect

Find files with SQL-like queries.
More information: <https://github.com/jhspetersson/fselect>.

- Select full path and size from temporary or config files in a given directory:

`fselect size, path from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` where name = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'*.cfg'</span>` or name = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'*.tmp'</span>

- Find square images:

`fselect path from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` where width = height`

- Find old-school rap 320kbps MP3 files:

`fselect path from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` where genre = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rap</span>` and bitrate = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">320</span>` and mp3_year lt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2000</span>

- Select only the first 5 results and output as JSON:

`fselect size, path from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` into json`

- Use SQL aggregate functions to calculate minimum, maximum and average size of files in a directory:

`fselect "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MIN(size), MAX(size), AVG(size), SUM(size), COUNT(*)</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`"`
