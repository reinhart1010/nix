---
layout: page
title: linux/flatpak (English)
description: "Build, install and run flatpak applications and runtimes."
content_hash: da96b8d4f44ddceccfab89234d02053ec3b08363
last_modified_at: 2024-08-27
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

`flatpak run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Install an application from a remote source:

`flatpak install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- List installed applications, ignoring runtimes:

`flatpak list --app`

- Update all installed applications and runtimes:

`flatpak update`

- Add a remote source:

`flatpak remote-add --if-not-exists `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_url</span>

- Remove an installed application:

`flatpak remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Remove all unused applications:

`flatpak remove --unused`

- Show information about an installed application:

`flatpak info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>
