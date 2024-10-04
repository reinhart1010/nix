---
layout: page
title: common/crane-digest (English)
description: "Get the digest of an image."
content_hash: f3f933aa2240bf96a0a186fba0a417881192bb64
last_modified_at: 2024-10-04
tldri18n_status: 2
---
# crane digest

Get the digest of an image.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Get the digest of an image:

`crane digest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>

- Print the full image reference by digest:

`crane digest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>` --full-ref`

- Specify path to tarball containing the image:

`crane digest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>` --tarball `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/tarball</span>

- Display help:

`crane digest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
