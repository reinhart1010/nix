---
layout: page
title: windows/attrib (English)
description: "Displays or changes file and directory attributes."
content_hash: 1c0771bc68e740da52f8fc3b350c91b4e990dbcd
related_topics:
  - title: 日本語 version
    url: /ja/windows/attrib.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/attrib.html
    icon: bi bi-globe
---
# attrib

Displays or changes file and directory attributes.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/attrib>.

- Display the attributes of the files in the current directory:

`attrib`

- Display the attributes of the files in the current directory and sub-directories:

`attrib /S`

- Display the attributes of the files and directories in the current directory and sub-directories:

`attrib /S /D`

- Add the read-only attribute to a file:

`attrib +R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">document.txt</span>

- Remove the system and hidden attributes of a file:

`attrib -S -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">document.txt</span>

- Add the hidden attribute to a directory:

`attrib +H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>
