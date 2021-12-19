---
layout: page
title: common/mycli (English)
description: "A command-line client for MySQL that can do auto-completion and syntax highlighting."
content_hash: fd8d2e0731e62dbd90df3a17b802f5c028ca66e3
---
# mycli

A command-line client for MySQL that can do auto-completion and syntax highlighting.
More information: <https://mycli.net>.

- Connect to a local database on port 3306, using the current user's username:

`mycli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Connect to a database (user will be prompted for a password):

`mycli -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Connect to a database on another host:

`mycli -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_host</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>
