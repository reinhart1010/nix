---
layout: page
title: common/phploc (English)
description: "Quickly measure the size and analyzing the structure of a PHP project."
content_hash: 150d901f1e829d6d139a336ed7165708229d350b
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# phploc

Quickly measure the size and analyzing the structure of a PHP project.
More information: <https://github.com/sebastianbergmann/phploc>.

- Analyze a directory and print the result:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Include only specific files from a comma-separated list (globs are allowed):

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --names '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1,path/to/file2,...</span>`'`

- Exclude specific files from a comma-separated list (globs are allowed):

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --names-exclude '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1,path/to/file2,...</span>`'`

- Exclude a specific directory from analysis:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/exclude_directory</span>

- Log the results to a specific CSV file:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --log-csv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Log the results to a specific XML file:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --log-xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Count PHPUnit test case classes and test methods:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --count-tests`
