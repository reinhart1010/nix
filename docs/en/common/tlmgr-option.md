---
layout: page
title: common/tlmgr-option (English)
description: "TeX Live settings manager."
content_hash: 6ee2f29f3f17a614d93e324c37fa2f4cc7d60b40
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tlmgr option

TeX Live settings manager.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- List all TeX Live settings:

`tlmgr option showall`

- List all currently set Tex Live settings:

`tlmgr option show`

- Print all TeX Live settings in JSON format:

`tlmgr option showall --json`

- Show the value of a specific TeX Live setting:

`tlmgr option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">setting</span>

- Modify the value of a specific TeX Live setting:

`tlmgr option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">setting</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Set TeX Live to get future updates from the internet after installing from DVD:

`tlmgr option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://mirror.ctan.org/systems/texlive/tlnet</span>
