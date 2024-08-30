---
layout: page
title: linux/dos2unix (English)
description: "Change DOS-style line endings to Unix-style."
content_hash: 04d8d6f11a1c60c9e3dbc86efd4a2ad0cbba79f7
last_modified_at: 2024-08-30
related_topics:
  - title: català version
    url: /ca/linux/dos2unix.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dos2unix.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dos2unix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dos2unix

Change DOS-style line endings to Unix-style.
Replaces CRLF with LF.
See also `unix2dos`, `unix2mac`, and `mac2unix`.
More information: <https://manned.org/dos2unix>.

- Change the line endings of a file:

`dos2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create a copy with Unix-style line endings:

`dos2unix -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new_file</span>

- Display file information:

`dos2unix -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Keep/add/remove Byte Order Mark:

`dos2unix --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
