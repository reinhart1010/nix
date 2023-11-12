---
layout: page
title: common/paste (English)
description: "Merge lines of files."
content_hash: 6dba12be94741a03cd3748c5908eaeb4cbd99de0
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# paste

Merge lines of files.
More information: <https://www.gnu.org/software/coreutils/paste>.

- Join all the lines into a single line, using TAB as delimiter:

`paste -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Join all the lines into a single line, using the specified delimiter:

`paste -s -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delimiter</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Merge two files side by side, each in its column, using TAB as delimiter:

`paste `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Merge two files side by side, each in its column, using the specified delimiter:

`paste -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delimiter</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Merge two files, with lines added alternatively:

`paste -d '\n' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>
