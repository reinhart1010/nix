---
layout: page
title: common/df (English)
description: "Display an overview of the filesystem disk space usage."
content_hash: 834646e7264ec6c91f2c756d4a75192939f7b16b
last_modified_at: 2024-01-07
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

Display an overview of the filesystem disk space usage.
More information: <https://pubs.opengroup.org/onlinepubs/9699919799.2018edition/utilities/df.html>.

- Display all filesystems and their disk usage using 512-byte units:

`df`

- Display the filesystem and its disk usage containing the given file or directory:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Use 1024-byte units when writing space figures:

`df -k`

- Display information in a portable way:

`df -P`
