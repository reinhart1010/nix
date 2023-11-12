---
layout: page
title: windows/find (English)
description: "Find a specified string in one or more files."
content_hash: c82aebfe743dc472f90f4c74c83e42e497cc7810
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/windows/find.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/find.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/find.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/find.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/find.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/find.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/find.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/find.html
    icon: bi bi-globe
tldri18n_status: 2
---
# find

Find a specified string in one or more files.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- Find lines that contain a specified string:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>

- Display lines that do not contain the specified string:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` /v`

- Display the count of lines that contain the specified string:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` /c`

- Display line numbers with the list of lines:

`find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` /n`
