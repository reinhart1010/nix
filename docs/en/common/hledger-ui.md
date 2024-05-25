---
layout: page
title: common/hledger-ui (English)
description: "Terminal UI (TUI) to `hledger`."
content_hash: 69151749f9d7587a9821429ee116531a8fa35ad5
last_modified_at: 2024-05-25
tldri18n_status: 2
---
# hledger-ui

Terminal UI (TUI) to `hledger`.
A robust, friendly plain text accounting app.
More information: <https://hledger.org/hledger-ui.html>.

- Start in the main menu screen, reading from the default journal file:

`hledger-ui`

- Start with a different color theme:

`hledger-ui --theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">terminal|greenterm|dark</span>

- Start in the balance sheet accounts screen, showing hierarchy down to level 3:

`hledger-ui --bs --tree --depth 3`

- Start in this account's screen, showing cleared transactions, and reload on change:

`hledger-ui --register `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assets:bank:checking</span>` --cleared --watch`

- Read two journal files, and show amounts as current value when known:

`hledger-ui --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/2024.journal</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/2024-prices.journal</span>` --value now`

- Show the manual in Info format, if possible:

`hledger-ui --info`

- Display help:

`hledger-ui --help`
