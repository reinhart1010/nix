---
layout: page
title: common/crane-validate (English)
description: "Validate that an image is well-formed."
content_hash: 4600b9b918c747f11a04f4d4235c7fbb5ec72777
last_modified_at: 2024-10-04
tldri18n_status: 2
---
# crane validate

Validate that an image is well-formed.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_validate.md>.

- Validate an image:

`crane validate`

- Skip downloading/digesting layers:

`crane validate --fast`

- Name of remote image to validate:

`crane validate --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>

- Path to tarball to validate:

`crane validate --tarball `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/tarball</span>

- Display help:

`crane validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
