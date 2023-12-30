---
layout: page
title: common/wireplumber (English)
description: "A modular session/policy manager for PipeWire and a GObject-based high-level library that wraps PipeWire’s API."
content_hash: ba8c87e2d87d7e61f0b68984f2a35f48af70d48c
last_modified_at: 2023-12-30
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wireplumber.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wireplumber

A modular session/policy manager for PipeWire and a GObject-based high-level library that wraps PipeWire’s API.
See also: `wpctl`, `pipewire`.
More information: <https://pipewire.pages.freedesktop.org/wireplumber/running-wireplumber-daemon.html>.

- Make WirePlumber start with the user session immediately (for systemd systems):

`systemctl --user --now enable wireplumber`

- Run WirePlumber, after `pipewire` is started (for non-systemd systems):

`wireplumber`

- Specify a different context configuration file:

`wireplumber --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display help:

`wireplumber --help`

- Display version:

`wirepumbler --version`
