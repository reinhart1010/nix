---
layout: page
title: common/tlmgr-generate (English)
description: "Remake configuration files from information stored locally."
content_hash: 56531d339dca86ceea30a86c9634f4fd47bb4c2c
last_modified_at: 2023-12-23
tldri18n_status: 2
---
# tlmgr generate

Remake configuration files from information stored locally.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- Remake the configuration file storing into a specific location:

`tlmgr generate --dest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>

- Remake the configuration file using a local configuration file:

`tlmgr generate --localcfg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_configuration_file</span>

- Run necessary programs after rebuilding configuration files:

`tlmgr generate --rebuild-sys`
