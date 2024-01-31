---
layout: page
title: common/goimports (English)
description: "Updates Go import lines, adding missing ones and removing unreferenced ones."
content_hash: f1199653ffcea586cdaa34a4323a1c23e3c3b36c
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# goimports

Updates Go import lines, adding missing ones and removing unreferenced ones.
More information: <https://godoc.org/golang.org/x/tools/cmd/goimports>.

- Display the completed import source file:

`goimports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.go</span>

- Write the result back to the source file instead of `stdout`:

`goimports -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.go</span>

- Display diffs and write the result back to the source file:

`goimports -w -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.go</span>

- Set the import prefix string after 3rd-party packages (comma-separated list):

`goimports -local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package1,path/to/package2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.go</span>
