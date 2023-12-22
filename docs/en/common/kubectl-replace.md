---
layout: page
title: common/kubectl-replace (English)
description: "Replace a resource by file or `stdin`."
content_hash: fa38a82b112e3d124a9a15bb3a659a19f79e9136
last_modified_at: 2023-12-22
tldri18n_status: 2
---
# kubectl replace

Replace a resource by file or `stdin`.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#replace>.

- Replace the resource using the resource definition file:

`kubectl replace -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yml</span>

- Replace the resource using the input passed into `stdin`:

`kubectl replace -f -`

- Force replace, delete and then re-create the resource:

`kubectl replace --force -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yml</span>
