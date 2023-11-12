---
layout: page
title: windows/replace (English)
description: "Replace files."
content_hash: d405bbfdb18e4c24006e22edd7263c67a73a009c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# replace

Replace files.
See also: `robocopy`, `move`, `copy`, and `del`.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/replace>.

- Replace the destination file with the one from the source directory:

`replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>

- Add files to the destination directory instead of replacing existing files:

`replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /a`

- Interactively copy multiple files, with a prompt before replacing or adding a destination file:

`replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /p`

- Replace even read only files:

`replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /r`

- Wait for you to insert a disk before it replaces files (originally to allow inserting a floppy disk):

`replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /w`

- Replace all files in subdirectories of the destination:

`replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /s`

- Replace only files in the destination directory which are older than the files in the source directory:

`replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /u`

- Display detailed usage information:

`replace /?`
