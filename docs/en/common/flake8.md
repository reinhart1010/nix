---
layout: page
title: common/flake8 (English)
description: "Check the style and quality of Python code."
content_hash: 589959ee27fd91d3c57670ff7309f55969c87f66
last_modified_at: 2024-02-15
related_topics:
  - title: italiano version
    url: /it/common/flake8.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flake8

Check the style and quality of Python code.
More information: <https://flake8.pycqa.org/>.

- Lint a file or directory recursively:

`flake8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Lint a file or directory recursively and show the line on which each error occurred:

`flake8 --show-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Lint a file or directory recursively and ignore a list of rules. (All available rules can be found at flake8rules.com):

`flake8 --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule1,rule2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Lint a file or directory recursively but exclude files matching the given globs or substrings:

`flake8 --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">substring1,glob2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
