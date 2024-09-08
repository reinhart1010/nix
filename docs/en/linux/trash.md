---
layout: page
title: linux/trash (English)
description: "Manage the trashcan/recycling bin."
content_hash: fdd2ae135b76e8f483a2c357d32dc8a40959b493
last_modified_at: 2024-09-08
related_topics:
  - title: Türkçe version
    url: /tr/linux/trash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# trash

Manage the trashcan/recycling bin.
More information: <https://github.com/andreafrancia/trash-cli>.

- Send a file to the trash:

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
