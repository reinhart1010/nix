---
layout: page
title: common/onefetch (English)
description: "Display project information and code statistics for a local Git repository."
content_hash: 942bfd1630cedc1c9c1045a07fd2d5e6360ba446
last_modified_at: 2024-10-02
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/onefetch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># onefetch

Display project information and code statistics for a local Git repository.
More information: <https://github.com/o2sh/onefetch/wiki>.

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
