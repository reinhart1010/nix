---
layout: page
title: common/tlmgr-platform (English)
description: "Manage TeX Live platforms."
content_hash: 8af4be5714fbf2d3b2ec6e09ae14b4c38180205f
last_modified_at: 2023-12-14
tldri18n_status: 2
---
# tlmgr platform

Manage TeX Live platforms.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- List all available platforms in the package repository:

`tlmgr platform list`

- Add the executables for a specific platform:

`sudo tlmgr platform add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform</span>

- Remove the executables for a specific platform:

`sudo tlmgr platform remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform</span>

- Auto-detect and switch to the current platform:

`sudo tlmgr platform set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto</span>

- Switch to a specific platform:

`sudo tlmgr platform set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform</span>
