---
layout: page
title: common/parallel-lint (English)
description: "Check the syntax of PHP files in parallel."
content_hash: 9ecc1e82b6dd1a3ce42006bf4e73909690734633
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# parallel-lint

Check the syntax of PHP files in parallel.
More information: <https://github.com/JakubOnderka/PHP-Parallel-Lint>.

- Lint a specific directory:

`parallel-lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Lint a directory using the specified number of parallel processes:

`parallel-lint -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">processes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Lint a directory, excluding the specified directory:

`parallel-lint --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/excluded_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Lint a directory of files using a comma-separated list of extension(s):

`parallel-lint -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php,html,phpt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Lint a directory and output the results as JSON:

`parallel-lint --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Lint a directory and show Git Blame results for rows containing errors:

`parallel-lint --blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
