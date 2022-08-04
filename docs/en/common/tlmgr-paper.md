---
layout: page
title: common/tlmgr-paper (English)
description: "Manage paper size options of an TeX Live installation."
content_hash: c0343003ab98bf3af3ad8192eb2c7a4f568fbca9
---
# tlmgr paper

Manage paper size options of an TeX Live installation.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- Show the default paper size used by all TeX Live programs:

`tlmgr paper`

- Set the default paper size for all TeX Live programs to A4:

`sudo tlmgr paper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a4</span>

- Show the default paper size used by a specific TeX Live program:

`tlmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdftex</span>` paper`

- Set the default paper size for a specific TeX Live program to A4:

`sudo tlmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdftex</span>` paper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a4</span>

- List all available paper sizes for a specific TeX Live program:

`tlmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdftex</span>` paper --list`

- Dump the default paper size used by all TeX Live programs in JSON format:

`tlmgr paper --json`
