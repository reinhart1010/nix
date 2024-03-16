---
layout: page
title: common/wdiff (English)
description: "Display word differences between text files."
content_hash: f873b5934398f5a55043adac6adf722af10e9bda
last_modified_at: 2024-03-16
tldri18n_status: 2
---
# wdiff

Display word differences between text files.
More information: <https://www.gnu.org/software/wdiff/>.

- Compare two files:

`wdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Ignore case when comparing:

`wdiff --ignore-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Display how many words are deleted, inserted or replaced:

`wdiff --statistics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>
