---
layout: page
title: common/df (English)
description: "Gives an overview of the filesystem disk space usage."
content_hash: 9782c458be24a7ae7896c753452692debd0acb6c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/df.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/df.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/df.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/df.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

Gives an overview of the filesystem disk space usage.
More information: <https://www.gnu.org/software/coreutils/df>.

- Display all filesystems and their disk usage:

`df`

- Display all filesystems and their disk usage in human-readable form:

`df -h`

- Display the filesystem and its disk usage containing the given file or directory:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Display statistics on the number of free inodes:

`df -i`

- Display filesystems but exclude the specified types:

`df -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>
