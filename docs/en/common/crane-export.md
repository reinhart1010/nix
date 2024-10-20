---
layout: page
title: common/crane-export (English)
description: "Export filesystem of a container image as a tarball."
content_hash: a9f7f6d5b0df632a7359676791fe0d5e273a9815
last_modified_at: 2024-10-20
related_topics:
  - title: 한국어 version
    url: /ko/common/crane-export.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane export

Export filesystem of a container image as a tarball.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Write tarball to `stdout`:

`crane export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>` -`

- Write tarball to file:

`crane export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/tarball</span>

- Read image from `stdin`:

`crane export - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename</span>
