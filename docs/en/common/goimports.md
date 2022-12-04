---
layout: page
title: common/goimports (English)
description: "Updates Go import lines, adding missing ones and removing unreferenced ones."
content_hash: e4a6840605b0c17944d3c882d37667ccefd90ca1
last_modified_at: 2022-12-04
---
# goimports

Updates Go import lines, adding missing ones and removing unreferenced ones.
More information: <https://godoc.org/golang.org/x/tools/cmd/goimports>.

- Display the completed import source file:

`goimports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.go`

- Write the result back to the source file instead of the standard output:

`goimports -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.go`

- Display diffs and write the result back to the source file:

`goimports -w -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.go`

- Set the import prefix string after 3rd-party packages (comma-separated list):

`goimports -local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.go`
