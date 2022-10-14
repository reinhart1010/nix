---
layout: page
title: common/flips (English)
description: "Create and apply patches for IPS and BPS files."
content_hash: fb24de37146927ce1d41e573d846efd602699e98
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># flips

Create and apply patches for IPS and BPS files.
More information: <https://github.com/Alcaro/Flips>.

- Start Flips to create and apply patches interactively:

`flips`

- Apply a patch and create a new ROM file:

`flips --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patch.bps</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rom.smc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hack.smc</span>

- Create a patch from two ROMs:

`flips --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rom.smc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hack.smc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patch.bps</span>
