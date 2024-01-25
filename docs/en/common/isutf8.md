---
layout: page
title: common/isutf8 (English)
description: "Check whether text files contain valid UTF-8."
content_hash: 02c8698eeff246440def22e39215b988438c51bb
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# isutf8

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
