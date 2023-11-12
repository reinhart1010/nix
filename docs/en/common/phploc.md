---
layout: page
title: common/phploc (English)
description: "A tool for quickly measuring the size and analyzing the structure of a PHP project."
content_hash: a7f8623617bfb39c97079d9f9661701271bba079
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# phploc

A tool for quickly measuring the size and analyzing the structure of a PHP project.
More information: <https://github.com/sebastianbergmann/phploc>.

- Analyze a directory and print the result:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Include only specific files from a comma-separated list (globs are allowed):

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --names `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">files</span>

- Exclude specific files from a comma-separated list (globs are allowed):

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --names-exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">files</span>

- Exclude a specific directory from analysis:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/exclude_directory</span>

- Log the results to a specific CSV file:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --log-csv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Log the results to a specific XML file:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --log-xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count PHPUnit test case classes and test methods:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --count-tests`
