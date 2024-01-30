---
layout: page
title: common/godoc (English)
description: "Show documentation for go packages."
content_hash: 7f9826036ed0318e763526141c03bfa1c831ed39
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# godoc

Show documentation for go packages.
More information: <https://godoc.org/>.

- Display help for a specific package:

`godoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fmt</span>

- Display help for the function "Printf" of "fmt" package:

`godoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fmt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Printf</span>

- Serve documentation as a web server on port 6060:

`godoc -http=:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6060</span>

- Create an index file:

`godoc -write_index -index_files=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Use the given index file to search the docs:

`godoc -http=:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6060</span>` -index -index_files=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
