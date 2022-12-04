---
layout: page
title: common/prettier (English)
description: "An opinionated code formatter for JavaScript, JSON, CSS, YAML, and more."
content_hash: 13665e838acdb70fb7bd0c65056765ab6e489179
last_modified_at: 2022-12-04
---
# prettier

An opinionated code formatter for JavaScript, JSON, CSS, YAML, and more.
More information: <https://prettier.io/>.

- Format a file and print the result to `stdout`:

`prettier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check if a specific file has been formatted:

`prettier --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Run with a specific configuration file:

`prettier --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Format a file or directory, replacing the original:

`prettier --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Format files or directories recursively using single quotes and no trailing commas:

`prettier --single-quote --trailing-comma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Format JavaScript and TypeScript files recursively, replacing the original:

`prettier --write "**/*.{js,jsx,ts,tsx}"`
