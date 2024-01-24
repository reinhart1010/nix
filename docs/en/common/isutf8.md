---
layout: page
title: common/isutf8 (English)
description: "Check whether text files contain valid UTF-8."
content_hash: 02c8698eeff246440def22e39215b988438c51bb
last_modified_at: 2024-01-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/isutf8.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># isutf8

Check whether text files contain valid UTF-8.
More information: <https://joeyh.name/code/moreutils/>.

- Check whether the specified files contain valid UTF-8:

`isutf8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Print errors using multiple lines:

`isutf8 --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Do not print anything to `stdout`, indicate the result merely with the exit code:

`isutf8 --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Only print the names of the files containing invalid UTF-8:

`isutf8 --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Same as `--list` but inverted, i.e., only print the names of the files containing valid UTF-8:

`isutf8 --invert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
