---
layout: page
title: common/hledger-web (English)
description: "Web interface and API to `hledger`."
content_hash: 3cd26ff9b9b4c93ef2ae7f5bb02b9c30abf83873
last_modified_at: 2024-05-25
tldri18n_status: 2
---
# hledger-web

Web interface and API to `hledger`.
A robust, friendly plain text accounting app.
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
