---
layout: page
title: linux/dolphin (English)
description: "KDE's file manager to manage files and directories."
content_hash: 88fb50d0d9aa8f166c5701a49c17bb1938550137
last_modified_at: 2024-04-04
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/dolphin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dolphin

KDE's file manager to manage files and directories.
See also: `nautilus`, `caja`, `thunar`, `ranger`.
More information: <https://apps.kde.org/dolphin/>.

- Launch the file manager:

`dolphin`

- Open specific directories:

`dolphin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Open with specific files or directories selected:

`dolphin --select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Open a new window:

`dolphin --new-window`

- Open specific directories in split view:

`dolphin --split `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory2</span>

- Launch the daemon (only required to use the D-Bus interface):

`dolphin --daemon`

- Display help:

`dolphin --help`
