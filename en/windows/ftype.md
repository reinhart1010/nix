---
layout: page
title: windows/ftype (English)
description: "Display or modify file types used for file extension association."
content_hash: d815de24c12a5453ebefb00a61e30d81d0f8207a
related_topics:
  - title: 中文 version
    url: /zh/windows/ftype.html
    icon: bi bi-globe
---
# ftype

Display or modify file types used for file extension association.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/ftype>.

- Display a list of all file types:

`ftype`

- Display the associated program for a specific file type:

`ftype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_type</span>

- Set the associated program for a specific file type:

`ftype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_type</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable_command</span>`"`
