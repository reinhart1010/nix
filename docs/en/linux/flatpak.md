---
layout: page
title: linux/flatpak (English)
description: "Build, install and run flatpak applications and runtimes."
content_hash: 017921a8bffb9268ce21d3bc031c55a5076b1811
last_modified_at: 2023-11-12
related_topics:
  - title: हिन्दी version
    url: /hi/linux/flatpak.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/flatpak.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/flatpak.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/flatpak.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flatpak

Build, install and run flatpak applications and runtimes.
More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- Run an installed application:

`flatpak run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Install an application from a remote source:

`flatpak install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- List all installed applications and runtimes:

`flatpak list`

- Update all installed applications and runtimes:

`flatpak update`

- Add a remote source:

`flatpak remote-add --if-not-exists `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_url</span>

- Remove an installed application:

`flatpak remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Remove all unused applications:

`flatpak remove --unused`

- Show information about an installed application:

`flatpak info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
