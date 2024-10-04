---
layout: page
title: common/crane-index-append (English)
description: "Append manifest to a remote index."
content_hash: c3d60abdaae75ad104a0f6cbe4fc26c23ec89bfe
last_modified_at: 2024-10-04
tldri18n_status: 2
---
# crane index append

Append manifest to a remote index.
This sub-command pushes an index based on an (optional) base index, with appended manifests.
The platform for appended manifests is inferred from the config file or omitted if that is infeasible.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_append.md>.

- Append manifest to a remote index:

`crane index append`

- Reference to manifests to append to the base index:

`crane index append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--manifest</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">manifest_name1 manifest_name2 ...</span>

- Tag to apply to resulting image:

`crane index append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>

- Empty base index will have Docker media types instead of OCI:

`crane index append --docker-empty-base`

- Append each of its children rather than the index itself (defaults true):

`crane index append --flatten`

- Display help:

`crane index append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
