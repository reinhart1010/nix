---
layout: page
title: windows/choco-uninstall (English)
description: "Uninstall one or more packages with Chocolatey."
content_hash: f559a7b23270871e284e795a761e08de98ff5c5a
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-uninstall.html
    icon: bi bi-globe
---
# choco uninstall

Uninstall one or more packages with Chocolatey.
More information: <https://chocolatey.org/docs/commands-uninstall>.

- Uninstall one or more space-separated packages:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package(s)</span>

- Uninstall a specific version of a package:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Confirm all prompts automatically:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --yes`

- Remove all dependencies when uninstalling:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --remove-dependencies`

- Uninstall all packages:

`choco uninstall all`
