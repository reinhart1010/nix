---
layout: page
title: common/tsort (English)
description: "Perform a topological sort."
content_hash: 85ef465bd1fd24d114b00054b043ddf34d3a3660
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/tsort.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tsort.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tsort

Perform a topological sort.
A common use is to show the dependency order of nodes in a directed acyclic graph.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/tsort-invocation.html>.

- Perform a topological sort consistent with a partial sort per line of input separated by blanks:

`tsort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Perform a topological sort consistent on strings:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UI Backend\nBackend Database\nDocs UI</span>`" | tsort`
