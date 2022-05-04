---
layout: page
title: linux/trash (English)
description: "A CLI for managing the trashcan / recycling bin."
content_hash: 9291aaaf4f2b557e3704de2d11475d3b31f864dc
related_topics:
  - title: Türkçe version
    url: /tr/linux/trash.html
    icon: bi bi-globe
---
# trash

A CLI for managing the trashcan / recycling bin.
More information: <https://github.com/andreafrancia/trash-cli>.

- Delete a file and send it to the trash:

`trash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- List all files in the trash:

`trash-list`

- Interactively restore a file from the trash:

`trash-restore`

- Empty the trash:

`trash-empty`

- Permanently delete all files in the trash which are older than 10 days:

`trash-empty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Remove all files in the trash, which match a specific blob pattern:

`trash-rm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.o</span>`"`

- Remove all files with a specific original location:

`trash-rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file_or_directory</span>
