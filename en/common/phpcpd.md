---
layout: page
title: common/phpcpd (English)
description: "A copy and paste detector for PHP code."
content_hash: 13c1ae21ea9300afa2f3ff09a788c5604ff58e04
---
# phpcpd

A copy and paste detector for PHP code.
More information: <https://github.com/sebastianbergmann/phpcpd>.

- Analyse duplicated code for a specific file or directory:

`phpcpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Analyse using fuzzy matching for variable names:

`phpcpd --fuzzy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Specify a minimum number of identical lines (defaults to 5):

`phpcpd --min-lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_lines</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Specify a minimum number of identical tokens (defaults to 70):

`phpcpd --min-tokens `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_tokens</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Exclude a directory from analysis (must be relative to the source):

`phpcpd --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/excluded_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Output the results to a PHP-CPD XML file:

`phpcpd --log-pmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/log_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
