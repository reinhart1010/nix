---
layout: page
title: windows/cd (English)
description: "Display the current working directory or move to a different directory."
content_hash: 7dd4bc0c1c9551d85bbc49de4ab578a1e7b6766f
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/windows/cd.html
    icon: bi bi-globe
  - title: čeština version
    url: /cs/windows/cd.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/cd.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/cd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cd.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/cd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/cd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cd.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/cd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cd

Display the current working directory or move to a different directory.
In PowerShell, this command is an alias of `Set-Location`. This documentation is based on the Command Prompt (`cmd`) version of `cd`.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- View documentation of the equivalent PowerShell command:

`tldr set-location`

- Display the path of the current directory:

`cd`

- Go to a specific directory in the same drive:

`cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- Go to a specific directory in a different [d]rive:

`cd /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- Go up to the parent of the current directory:

`cd ..`

- Go to the home directory of the current user:

`cd %userprofile%`

- Go to root of current drive:

`cd \`
