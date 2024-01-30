---
layout: page
title: windows/xcopy (English)
description: "Copy files and directory trees."
content_hash: 9ac16c159acb6b472c6bb38053349c2d0ef50a98
last_modified_at: 2024-01-30
related_topics:
  - title: Deutsch version
    url: /de/windows/xcopy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/xcopy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/xcopy.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/xcopy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/xcopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcopy

Copy files and directory trees.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- Copy the file(s) to the specified destination:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>

- List files that will be copied before copying:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /p`

- Copy the directory structure only, excluding files:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /t`

- Include empty directories when copying:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /e`

- Keep the source ACL in the destination:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /o`

- Allow resuming when network connection is lost:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /z`

- Disable the prompt when the file exists in the destination:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /y`

- Display help:

`xcopy /?`
