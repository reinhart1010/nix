---
layout: page
title: common/rmlint (English)
description: "Find space waste and other broken things on your filesystem."
content_hash: 9f4bc13607ece1bb3b41646f0eb2847c7a5690f5
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/rmlint.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rmlint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rmlint

Find space waste and other broken things on your filesystem.
More information: <https://rmlint.readthedocs.io/en/latest/rmlint.1.html>.

- Check directories for duplicated, empty and broken files:

`rmlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Check for duplicates bigger than a specific size, preferably keeping files in tagged directories (after the double slash):

`rmlint -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1MB</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` // `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/original_directory</span>

- Check for space wasters, keeping everything in the untagged directories:

`rmlint --keep-all-untagged `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` // `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/original_directory</span>

- Delete duplicate files found by an execution of `rmlint`:

`./rmlint.sh`

- Find duplicate directory trees based on data, ignoring names:

`rmlint --merge-directories `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Mark files at lower path [d]epth as originals, on tie choose shorter [l]ength:

`rmlint --rank-by=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Find files with identical filename and contents, and link rather than delete the duplicates:

`rmlint -c sh:link --match-basename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Use `data` as master directory. Find only duplicates in backup that are also in `data`. Do not delete any files in `data`:

`rmlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/backup</span>` // `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/data</span>` --keep-all-tagged --must-match-tagged`
