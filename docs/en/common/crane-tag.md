---
layout: page
title: common/crane-tag (English)
description: "Efficiently tag a remote image without downloading it, which differs from the `copy` command."
content_hash: 05349e3d99959b90ada33b8b102ea10a048a963d
last_modified_at: 2024-10-04
tldri18n_status: 2
---
# crane tag

Efficiently tag a remote image without downloading it, which differs from the `copy` command.
It skips the layer existence checks because we know the manifest already exists making it slightly faster.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_tag.md>.

- Tag remote image:

`crane tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>

- Display help:

`crane tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
