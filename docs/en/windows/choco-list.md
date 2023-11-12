---
layout: page
title: windows/choco-list (English)
description: "Display a list of packages with Chocolatey."
content_hash: 23d34164f3eb7eb151def7325a45d25e65cee580
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-list.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-list.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-list.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco list

Display a list of packages with Chocolatey.
More information: <https://chocolatey.org/docs/commands-list>.

- Display all available packages:

`choco list`

- Display all locally installed packages:

`choco list --local-only`

- Display a list including local programs:

`choco list --include-programs`

- Display only approved packages:

`choco list --approved-only`

- Specify a custom source to display packages from:

`choco list --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|alias</span>

- Provide a username and password for authentication:

`choco list --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
