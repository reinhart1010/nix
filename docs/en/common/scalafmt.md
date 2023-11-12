---
layout: page
title: common/scalafmt (English)
description: "Code formatter for Scala."
content_hash: d7c4f5d02346bc172bbcf1551edfc82f65814975
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# scalafmt

Code formatter for Scala.
Configurations are stored in the `.scalafmt.conf` file.
More information: <https://scalameta.org/scalafmt>.

- Reformat all `.scala` files in the current directory recursively:

`scalafmt`

- Reformat specific files or directories with a custom formatting configuration:

`scalafmt --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/.scalafmt.conf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>

- Check if files are correctly formatted, returning `0` if all files respect the formatting style:

`scalafmt --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/.scalafmt.conf</span>` --test`

- Exclude files or directories:

`scalafmt --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>

- Format only files that were edited against the current Git branch:

`scalafmt --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/.scalafmt.conf</span>` --mode diff`
