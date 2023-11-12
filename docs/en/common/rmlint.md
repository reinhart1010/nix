---
layout: page
title: common/rmlint (English)
description: "Find space waste and other broken things on your filesystem."
content_hash: 58146b239819d68cce751620bce1e02ab7e8b73d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rmlint

Find space waste and other broken things on your filesystem.
More information: <https://rmlint.readthedocs.io/en/latest/rmlint.1.html>.

- Check directories for duplicated, empty and broken files:

`rmlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Check for space wasters, preferably keeping files in tagged directories (after the double slash):

`rmlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` // `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/original_directory</span>

- Check for space wasters, keeping everything in the untagged directories:

`rmlint --keep-all-untagged `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` // `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/original_directory</span>

- Delete duplicate files found by an execution of `rmlint`:

`./rmlint.sh`

- Find duplicate directory trees:

`rmlint --merge-directories `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Mark files at lower path [d]epth as originals, on tie choose shorter [l]ength:

`rmlint --rank-by=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Find only duplicates that have the same filename in addition to the same contents:

`rmlint --match-basename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Find only duplicates that have the same extension in addition to the same contents:

`rmlint --match-extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
