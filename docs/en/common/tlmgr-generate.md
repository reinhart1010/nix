---
layout: page
title: common/tlmgr-generate (English)
description: "Remake configuration files from information stored locally."
content_hash: 56531d339dca86ceea30a86c9634f4fd47bb4c2c
last_modified_at: 2023-12-22
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-generate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr generate

Remake configuration files from information stored locally.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- Remake the configuration file storing into a specific location:

`tlmgr generate --dest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>

- Remake the configuration file using a local configuration file:

`tlmgr generate --localcfg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_configuration_file</span>

- Run necessary programs after rebuilding configuration files:

`tlmgr generate --rebuild-sys`
