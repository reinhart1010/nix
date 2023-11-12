---
layout: page
title: windows/ftype (English)
description: "Display or modify file types used for file extension association."
content_hash: 772cf9a8f578e653182ab6782df96e6b77cb9382
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/windows/ftype.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ftype

Display or modify file types used for file extension association.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftype>.

- Display a list of all file types:

`ftype`

- Display the associated program for a specific file type:

`ftype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_type</span>

- Set the associated program for a specific file type:

`ftype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_type</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable_file</span>`"`
