---
layout: page
title: windows/choco-info (English)
description: "Display detailed information about a package with Chocolatey."
content_hash: 820f72b343d1d1915c9f030e90e935b686c5714f
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-info.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/choco-info.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-info.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-info.html
    icon: bi bi-globe
---
# choco info

Display detailed information about a package with Chocolatey.
More information: <https://chocolatey.org/docs/commands-info>.

- Display information on a specific package:

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display information for a local package only:

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --local-only`

- Specify a custom source to receive packages information from:

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|alias</span>

- Provide a username and password for authentication:

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
