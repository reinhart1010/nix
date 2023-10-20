---
layout: page
title: common/kubectl-replace (English)
description: "Replace a resource by file or `stdin`."
content_hash: ef5f4ee0a7666f083a891a4d6fa2dc1cf9721c81
last_modified_at: 2023-10-20
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kubctl replace

Replace a resource by file or `stdin`.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#replace>.

- Replace the resource using the resource definition file:

`kubectl replace -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yml</span>

- Replace the resource using the input passed into `stdin`:

`kubectl replace -f -`

- Force replace, delete and then re-create the resource:

`kubectl replace --force -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yml</span>
