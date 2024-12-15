---
layout: page
title: linux/kwallet-query (English)
description: "Read and write to a KDE Wallet."
content_hash: 5d54c96460c7ee7e92e8e933fefe3696c1e3a95b
last_modified_at: 2024-12-15
tldri18n_status: 2
---
# kwallet-query

Read and write to a KDE Wallet.
More information: <https://manned.org/kwallet-query>.

- List all entries in the `Passwords` folder of `kdewallet`:

`kwallet-query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kdewallet</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list-entries</span>

- List all entries in a specific folder:

`kwallet-query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kdewallet</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list-entries</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--folder</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">folder_name</span>

- List all available folders:

`kwallet-query  `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kdewallet</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list-entries</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--folder</span>` ""`
