---
layout: page
title: osx/hdiutil (English)
description: "Utility to create and manage disk images."
content_hash: 92c143d514c965f4afa6e273dd69c310320f58dd
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/osx/hdiutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hdiutil

Utility to create and manage disk images.
More information: <https://ss64.com/osx/hdiutil.html>.

- Mount an image:

`hdiutil attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>

- Unmount an image:

`hdiutil detach /Volumes/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_file</span>

- List mounted images:

`hdiutil info`

- Create an ISO image from the contents of a directory:

`hdiutil makehybrid -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
