---
layout: page
title: linux/unix2mac (English)
description: "Change Unix-style line endings to macOS-style."
content_hash: 95421c01b26a92449433fa69a2157bbb8912e662
last_modified_at: 2024-08-30
related_topics:
  - title: 中文 version
    url: /zh/linux/unix2mac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unix2mac

Change Unix-style line endings to macOS-style.
Replaces LF with CR.
See also `unix2dos`, `dos2unix`, and `mac2unix`.
More information: <https://waterlan.home.xs4all.nl/dos2unix.html>.

- Change the line endings of a file:

`unix2mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create a copy with macOS-style line endings:

`unix2mac -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new_file</span>

- Display file information:

`unix2mac -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Keep/add/remove Byte Order Mark:

`unix2mac --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
