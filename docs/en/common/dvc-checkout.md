---
layout: page
title: common/dvc-checkout (English)
description: "Checkout data files and directories from cache."
content_hash: c938196deb69e8feee7da8448859182c87056891
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/dvc-checkout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dvc checkout

Checkout data files and directories from cache.
More information: <https://dvc.org/doc/command-reference/checkout>.

- Checkout the latest version of all target files and directories:

`dvc checkout`

- Checkout the latest version of a specified target:

`dvc checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Checkout a specific version of a target from a different Git commit/tag/branch:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash|tag|branch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` && dvc checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>
