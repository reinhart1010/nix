---
layout: page
title: common/crane-flatten (English)
description: "Flatten an image's layers into a single layer."
content_hash: ba253e97fb3245e6862c33c303ee042ff066bd88
last_modified_at: 2024-10-04
tldri18n_status: 2
---
# crane flatten

Flatten an image's layers into a single layer.
Pushes digest to original image repository if no tags are specified.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Flatten an image:

`crane flatten`

- Apply new tag to flattened image:

`crane flatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>

- Display help:

`crane flatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
