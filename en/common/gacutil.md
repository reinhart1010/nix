---
layout: page
title: common/gacutil (English)
description: "Global Assembly Cache (CAG) management utility."
content_hash: 0b23aea67011d7aaa9488361428e2694d0668445
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gacutil

Global Assembly Cache (CAG) management utility.
More information: <https://manned.org/gacutil>.

- Install the specified assembly into GAC:

`gacutil -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>

- Uninstall the specified assembly from GAC:

`gacutil -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assembly_display_name</span>

- Print the content of GAC:

`gacutil -l`
