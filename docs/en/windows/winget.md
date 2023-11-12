---
layout: page
title: windows/winget (English)
description: "Windows Package Manager."
content_hash: dbc426cbea9a0abec7bf6cc98080cb171a388409
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/winget.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/winget.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/winget.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/winget.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/winget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/winget.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/winget.html
    icon: bi bi-globe
tldri18n_status: 2
---
# winget

Windows Package Manager.
More information: <https://learn.microsoft.com/windows/package-manager/winget>.

- Install a package:

`winget install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package (Note: `remove` can also be used instead of `uninstall`):

`winget uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display information about a package:

`winget show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search for a package:

`winget search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade all packages to the latest versions:

`winget upgrade --all`

- List all packages installed that can be managed with `winget`:

`winget list --source winget`

- Import packages from a file, or export installed packages to a file:

`winget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import|export</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--import-file|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Validate manifests before submitting a PR to the winget-pkgs repository:

`winget validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/manifest</span>
