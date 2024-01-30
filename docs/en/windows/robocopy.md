---
layout: page
title: windows/robocopy (English)
description: "Robust File and Folder Copy."
content_hash: 29ff303cdaac74c682f1bd5d80fecf24ac6d1f1e
last_modified_at: 2024-01-30
related_topics:
  - title: Deutsch version
    url: /de/windows/robocopy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/robocopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# robocopy

Robust File and Folder Copy.
By default files will only be copied if the source and destination have different time stamps or different file sizes.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/robocopy>.

- Copy all `.jpg` and `.bmp` files from one directory to another:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.bmp</span>

- Copy all files and subdirectories, including empty ones:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /E`

- Mirror/Sync a directory, deleting anything not in source and include all attributes and permissions:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /MIR /COPYALL`

- Copy all files and subdirectories, excluding source files that are older than destination files:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /E /XO`

- List all files 50 MB or larger instead of copying them:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /MIN:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">52428800</span>` /L`

- Allow resuming if network connection is lost and limit retries to 5 and wait time to 15 sec:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /Z /R:5 /W:15`

- Display help:

`robocopy /?`
