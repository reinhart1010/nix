---
layout: page
title: linux/flatpak-run (English)
description: "Run flatpak applications and runtimes."
content_hash: 8fbb5b80dc34ada83bf88db0e9fa4ae5a492ad56
last_modified_at: 2024-08-28
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
