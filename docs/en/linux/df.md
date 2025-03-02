---
layout: page
title: linux/df (English)
description: "Display an overview of the filesystem disk space usage."
content_hash: 15445d40ec4a9c97fe24d72ed239198efd9d554e
last_modified_at: 2025-03-02
related_topics:
  - title: 日本語 version
    url: /ja/linux/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

Display an overview of the filesystem disk space usage.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html>.

- Display all filesystems and their disk usage:

`df`

- Display all filesystems and their disk usage in human-readable form:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--human-readable</span>

- Display the filesystem and its disk usage containing the given file or directory:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Include statistics on the number of free inodes:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--inodes</span>

- Display filesystems but exclude the specified types:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-x|--exclude-type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-x|--exclude-type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>

- Display filesystem types:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-T|--print-type</span>
