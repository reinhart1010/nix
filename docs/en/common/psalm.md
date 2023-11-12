---
layout: page
title: common/psalm (English)
description: "A static analysis tool for finding errors in PHP applications."
content_hash: 45203cd7046a360b3dc80548bf837b8e461777b6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# psalm

A static analysis tool for finding errors in PHP applications.
More information: <https://psalm.dev>.

- Generate a Psalm configuration:

`psalm --init`

- Analyze the current working directory:

`psalm`

- Analyze a specific directory or file:

`psalm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Analyze a project with a specific configuration file:

`psalm --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/psalm.xml</span>

- Include informational findings in the output:

`psalm --show-info`

- Analyze a project and display statistics:

`psalm --stats`

- Analyze a project in parallel with 4 threads:

`psalm --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>
