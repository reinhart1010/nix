---
layout: page
title: common/var-dump-server (English)
description: "Symfony dump server."
content_hash: acc701e0c33b5e22f9ee44dc112b1e932c80a320
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# var-dump-server

Symfony dump server.
Collects data dumped by the Symfony VarDumper component.
More information: <https://symfony.com/doc/current/components/var_dumper.html#the-dump-server>.

- Start the server:

`var-dump-server`

- Dump the data in an HTML file:

`var-dump-server --format=html > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.html</span>

- Make the server listen on a specific address and port:

`var-dump-server --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1:9912</span>
