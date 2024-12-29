---
layout: page
title: linux/flatpak-run (English)
description: "Run flatpak applications and runtimes."
content_hash: 2cba7f7f74cac5b7b961389e27abb3c8c06e358c
last_modified_at: 2024-12-29
related_topics:
  - title: español version
    url: /es/linux/flatpak-run.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/flatpak-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flatpak run

Run flatpak applications and runtimes.
More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-run>.

- Run an installed application:

`flatpak run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Run an installed application from a specific branch e.g. stable, beta, master:

`flatpak run --branch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|beta|master|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Run an interactive shell inside a flatpak:

`flatpak run --command=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Run an installed application with a specific runtime version:

`flatpak run --runtime-version=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24.08|master|stable|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Run an installed application with a different runtime (but same version number):

`flatpak run --runtime=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.freedesktop.Sdk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>
