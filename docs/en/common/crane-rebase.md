---
layout: page
title: common/crane-rebase (English)
description: "Rebase an image onto a new base image."
content_hash: 09503a55674633ad7d54854ae0880666c97e5c39
last_modified_at: 2024-10-04
tldri18n_status: 2
---
# crane rebase

Rebase an image onto a new base image.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_rebase.md>.

- Rebase image:

`crane rebase`

- New base image to insert:

`crane rebase --new_base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>

- Old base image to remove:

`crane rebase --old_base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>

- Tag to apply to rebased image:

`crane rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>

- Display help:

`crane rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
