---
layout: page
title: common/tsort (English)
description: "Perform a topological sort."
content_hash: 6b79a26a94a595cbf5535ac1f5e981effbd4bfba
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tsort

Perform a topological sort.
A common use is to show the dependency order of nodes in a directed acyclic graph.
More information: <https://www.gnu.org/software/coreutils/tsort>.

- Perform a topological sort consistent with a partial sort per line of input separated by blanks:

`tsort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Perform a topological sort consistent on strings:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UI Backend\nBackend Database\nDocs UI</span>`" | tsort`
