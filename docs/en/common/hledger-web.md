---
layout: page
title: common/hledger-web (English)
description: "A web interface and API for `hledger`, a robust, friendly plain text accounting app."
content_hash: 31bffd12f49e5884ac556c5021f215a08246a757
last_modified_at: 2024-05-30
tldri18n_status: 2
---
# hledger-web

A web interface and API for `hledger`, a robust, friendly plain text accounting app.
More information: <https://hledger.org/hledger-web.html>.

- Start the web app, and a browser if possible, for local viewing and adding only:

`hledger-web`

- As above but with a specified file, and allow editing of existing data:

`hledger-web --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.journal</span>` --allow edit`

- Start just the web app, and accept incoming connections to the specified host and port:

`hledger-web --serve --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my.host.name</span>` --port 8000`

- Start just the web app's JSON API, and allow only read access:

`hledger-web --serve-api --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my.host.name</span>` --allow view`

- Show amounts converted to current market value in your base currency when known:

`hledger-web --value now --infer-market-prices`

- Show the manual in Info format if possible:

`hledger-web --info`

- Display help:

`hledger-web --help`
