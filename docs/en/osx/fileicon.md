---
layout: page
title: osx/fileicon (English)
description: "A macOS CLI to manage custom file and folder icons."
content_hash: e7dfd8a1a0484b7776f1c6a9520bd2215288299f
last_modified_at: 2023-02-20
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/osx/fileicon.html
    icon: bi bi-globe
---
# fileicon

A macOS CLI to manage custom file and folder icons.
More information: <https://github.com/mklement0/fileicon>.

- Set a custom icon for a specific file or directory:

`fileicon set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/icon_file.png</span>

- Remove a custom icon from a specific file or directory:

`fileicon rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Save the custom icon of a file or directory as a `.icns` file into the current directory:

`fileicon get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Test if a specific file or directory has a custom icon:

`fileicon test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
