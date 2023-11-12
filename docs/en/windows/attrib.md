---
layout: page
title: windows/attrib (English)
description: "Display or change attributes of files or directories."
content_hash: afe758167084fcc3a5705002ab6710f0b240e95c
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/windows/attrib.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/attrib.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/attrib.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/attrib.html
    icon: bi bi-globe
tldri18n_status: 2
---
# attrib

Display or change attributes of files or directories.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/attrib>.

- Display all set attributes of files in the current directory:

`attrib`

- Display all set attributes of files in a specific directory:

`attrib `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- Display all set attributes of files and [d]irectories in the current directory:

`attrib /d`

- Display all set attributes of files in the current directory and [s]ub-directories:

`attrib /s`

- Add the `[r]ead-only` or `[a]rchive` or `[s]ystem` or `[h]idden` or `not content [i]ndexed` attribute to files or directories:

`attrib +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">r|a|s|h|i</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory1 path\to\file_or_directory2 ...</span>

- Remove a specific attribute of files or directories:

`attrib -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">r|a|s|h|i</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory1 path\to\file_or_directory2 ...</span>
