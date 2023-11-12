---
layout: page
title: common/goimports (English)
description: "Updates Go import lines, adding missing ones and removing unreferenced ones."
content_hash: 44365fdd9a2d17bd3c5c3335512b304d881a263b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# goimports

Updates Go import lines, adding missing ones and removing unreferenced ones.
More information: <https://godoc.org/golang.org/x/tools/cmd/goimports>.

- Display the completed import source file:

`goimports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.go`

- Write the result back to the source file instead of `stdout`:

`goimports -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.go`

- Display diffs and write the result back to the source file:

`goimports -w -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.go`

- Set the import prefix string after 3rd-party packages (comma-separated list):

`goimports -local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.go`
