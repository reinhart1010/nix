---
layout: page
title: windows/choco-upgrade (English)
description: "Upgrade one or more packages with Chocolatey."
content_hash: 2add3de547acade811d9cc39b9653e8b6b2d0a95
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco upgrade

Upgrade one or more packages with Chocolatey.
More information: <https://chocolatey.org/docs/commands-upgrade>.

- Upgrade one or more packages:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Upgrade to a specific version of a package:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Upgrade all packages:

`choco upgrade all`

- Upgrade all except specified comma-separated packages:

`choco upgrade all --except "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1,package2,...</span>`"`

- Confirm all prompts automatically:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --yes`

- Specify a custom source to receive packages from:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|alias</span>

- Provide a username and password for authentication:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
