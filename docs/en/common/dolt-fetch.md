---
layout: page
title: common/dolt-fetch (English)
description: "Download objects and refs from another repository."
content_hash: b9ed80238af8a0d46a68e2ea6c98b3c342b2ef1e
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dolt fetch

Download objects and refs from another repository.
More information: <https://github.com/dolthub/dolt>.

- Fetch the latest changes from the default remote upstream repository (origin):

`dolt fetch`

- Fetch latest changes from a specific remote upstream repository:

`dolt fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Update branches with the current state of the remote, overwriting any conflicting history:

`dolt fetch -f`
