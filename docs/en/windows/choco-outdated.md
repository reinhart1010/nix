---
layout: page
title: windows/choco-outdated (English)
description: "Check for outdated packages with Chocolatey."
content_hash: 9d8939f9fcbc76402327931fb7dbd9c49a3d2e19
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-outdated.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-outdated.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-outdated.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-outdated.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-outdated.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco outdated

Check for outdated packages with Chocolatey.
More information: <https://chocolatey.org/docs/commands-outdated>.

- Display a list of outdated packages in table format:

`choco outdated`

- Ignore pinned packages in the output:

`choco outdated --ignore-pinned`

- Specify a custom source to check packages from:

`choco outdated --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|alias</span>

- Provide a username and password for authentication:

`choco outdated --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
