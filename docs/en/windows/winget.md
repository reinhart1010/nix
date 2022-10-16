---
layout: page
title: windows/winget (English)
description: "Windows Package Manager CLI."
content_hash: 6295d0b1841097e41d00697ed60a040d60435f3f
related_topics:
  - title: Deutsch version
    url: /de/windows/winget.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/winget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/winget.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/winget.html
    icon: bi bi-globe
---
# winget

Windows Package Manager CLI.
More information: <https://learn.microsoft.com/windows/package-manager/winget>.

- Install a package:

`winget install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display information about a package:

`winget show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search for a package:

`winget search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade all packages to latest versions:

`winget upgrade --all`

- List all packages installed that can be managed with winget:

`winget list --source winget`
