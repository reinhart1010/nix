---
layout: page
title: common/dolt-fetch (English)
description: "Download objects and refs from another repository."
content_hash: fdb365777e787eb4fbd4b8999f775e115aa329ff
last_modified_at: 2023-11-20
tldri18n_status: 2
---
# dolt fetch

Download objects and refs from another repository.
More information: <https://docs.dolthub.com/cli-reference/cli#dolt-fetch>.

- Fetch the latest changes from the default remote upstream repository (origin):

`dolt fetch`

- Fetch latest changes from a specific remote upstream repository:

`dolt fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Update branches with the current state of the remote, overwriting any conflicting history:

`dolt fetch -f`
