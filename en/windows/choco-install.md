---
layout: page
title: windows/choco-install (English)
description: "Install one or more packages with Chocolatey."
content_hash: 45e47307f1c978ecc14e054052bacc4060a2e748
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-install.html
    icon: bi bi-globe
---
# choco install

Install one or more packages with Chocolatey.
More information: <https://chocolatey.org/docs/commands-install>.

- Install one or more space-separated packages:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package(s)</span>

- Install packages from a custom configuration file:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/packages.config</span>

- Install a specific nuspec or nupkg file:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Install a specific version of a package:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Allow installing multiple versions of a package:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --allow-multiple`

- Confirm all prompts automatically:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --yes`

- Specify a custom source to receive packages from:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|alias</span>

- Provide a username and password for authentication:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
