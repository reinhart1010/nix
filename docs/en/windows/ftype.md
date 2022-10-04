---
layout: page
title: windows/ftype (English)
description: "Display or modify file types used for file extension association."
content_hash: a74ca3fa6656e691afeeafe53d489bb150a71b61
related_topics:
  - title: 中文 version
    url: /zh/windows/ftype.html
    icon: bi bi-globe
---
# ftype

Display or modify file types used for file extension association.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftype>.

- Display a list of all file types:

`ftype`

- Display the associated program for a specific file type:

`ftype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_type</span>

- Set the associated program for a specific file type:

`ftype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_type</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable_command</span>`"`
