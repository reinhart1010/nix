---
layout: page
title: osx/du (English)
description: "Disk usage: estimate and summarize file and directory space usage."
content_hash: d5b6e5799caad0bae31060aea1ddcd5c150de1b1
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/du.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/osx/du.html
    icon: bi bi-globe
tldri18n_status: 2
---
# du

Disk usage: estimate and summarize file and directory space usage.
More information: <https://keith.github.io/xcode-man-pages/du.1.html>.

- List the sizes of a directory and any subdirectories, in the given unit (KiB/MiB/GiB):

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- List the sizes of a directory and any subdirectories, in human-readable form (i.e. auto-selecting the appropriate unit for each size):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Show the size of a single directory, in human-readable units:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- List the human-readable sizes of a directory and of all the files and directories within it:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- List the human-readable sizes of a directory and any subdirectories, up to N levels deep:

`du -h -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- List the human-readable size of all `.jpg` files in subdirectories of the current directory, and show a cumulative total at the end:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
