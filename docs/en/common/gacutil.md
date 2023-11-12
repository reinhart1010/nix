---
layout: page
title: common/gacutil (English)
description: "Global Assembly Cache (CAG) management utility."
content_hash: 0b23aea67011d7aaa9488361428e2694d0668445
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gacutil

Global Assembly Cache (CAG) management utility.
More information: <https://manned.org/gacutil>.

- Install the specified assembly into GAC:

`gacutil -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>

- Uninstall the specified assembly from GAC:

`gacutil -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assembly_display_name</span>

- Print the content of GAC:

`gacutil -l`
