---
layout: page
title: osx/hdiutil (English)
description: "Utility to create and manage disk images."
content_hash: 07e1012466b135f905793ce339d6f38ec2e35153
last_modified_at: 2024-01-31
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/osx/hdiutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hdiutil

Utility to create and manage disk images.
More information: <https://keith.github.io/xcode-man-pages/hdiutil.1.html>.

- Mount an image:

`hdiutil attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>

- Unmount an image:

`hdiutil detach /Volumes/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_file</span>

- List mounted images:

`hdiutil info`

- Create an ISO image from the contents of a directory:

`hdiutil makehybrid -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
