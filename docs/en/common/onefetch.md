---
layout: page
title: common/onefetch (English)
description: "Display project information and code statistics for a local Git repository."
content_hash: cb810098fbe0cf7fecee21b1dc0c603b1b616072
last_modified_at: 2024-10-05
tldri18n_status: 2
---
# onefetch

Display project information and code statistics for a local Git repository.
More information: <https://github.com/o2sh/onefetch/wiki/command-line-options>.

- Display statistics for the Git repository in the current working directory:

`onefetch`

- Display statistics for the Git repository in the specified directory:

`onefetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Ignore commits made by bots:

`onefetch --no-bots`

- Ignore merge commits:

`onefetch --no-merges`

- Don't print the ASCII art of the language logo:

`onefetch --no-art`

- Show `n` authors, languages, or file churns (default: 3, 6, and 3 respectively):

`onefetch --number-of-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">authors|languages|file-churns</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Ignore the specified files and directories:

`onefetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--exclude</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory|regular_expression</span>

- Only detect languages from the specified categories (default: programming and markup):

`onefetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-T|--type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programming|markup|prose|data</span>
