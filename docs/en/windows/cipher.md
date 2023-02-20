---
layout: page
title: windows/cipher (English)
description: "Display or alter the encryption of directories and files on NTFS volumes."
content_hash: d17a1486fee4c040168998eedcafc4139ab687ce
last_modified_at: 2023-02-20
related_topics:
  - title: Deutsch version
    url: /de/windows/cipher.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cipher.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cipher.html
    icon: bi bi-globe
---
# cipher

Display or alter the encryption of directories and files on NTFS volumes.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cipher>.

- Display information about a specific encrypted file or directory:

`cipher /c:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>

- [e]ncrypt a file or directory (files added later to the directory are also encrypted as the directory is marked):

`cipher /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>

- [d]ecrypt a file or directory:

`cipher /d:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>

- Securely remove a file or directory:

`cipher /w:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>
