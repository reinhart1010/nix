---
layout: page
title: common/psalm (English)
description: "A static analysis tool for finding errors in PHP applications."
content_hash: 98853cfdd6756ea117042be81625ebd7325da6cf
---
# psalm

A static analysis tool for finding errors in PHP applications.
More information: <https://psalm.dev>.

- Generate a Psalm configuration:

`psalm --init`

- Analyse the current working directory:

`psalm`

- Analyse a specific directory or file:

`psalm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Analyse a project with a specific configuration file:

`psalm --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/psalm.xml</span>

- Include informational findings in the output:

`psalm --show-info`

- Analyse a project and display statistics:

`psalm --stats`

- Analyse a project in parallel with 4 threads:

`psalm --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>
