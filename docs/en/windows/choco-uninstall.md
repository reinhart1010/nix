---
layout: page
title: windows/choco-uninstall (English)
description: "Uninstall one or more packages with Chocolatey."
content_hash: f036b4a357545f79946b6bd9f54523d447b1e61c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-uninstall.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco uninstall

Uninstall one or more packages with Chocolatey.
More information: <https://chocolatey.org/docs/commands-uninstall>.

- Uninstall one or more space-separated packages:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Uninstall a specific version of a package:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Confirm all prompts automatically:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --yes`

- Remove all dependencies when uninstalling:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --remove-dependencies`

- Uninstall all packages:

`choco uninstall all`
