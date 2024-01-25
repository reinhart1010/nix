---
layout: page
title: common/ss-local (English)
description: "Run a Shadowsocks client as a SOCKS5 proxy."
content_hash: ee34178d6b485741705eb2a64665bb55c7d3ff9a
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# ss-local

Run a Shadowsocks client as a SOCKS5 proxy.
More information: <https://github.com/shadowsocks/shadowsocks-libev/blob/master/doc/ss-local.asciidoc>.

- Run a Shadowsocks proxy by specifying the host, server port, local port, password, and encryption method:

`ss-local -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_port</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local port</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encrypt_method</span>

- Run a Shadowsocks proxy by specifying the configuration file:

`ss-local -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config/file.json</span>

- Use a plugin to run the proxy client:

`ss-local --plugin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>` --plugin-opts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_options</span>

- Enable TCP fast open:

`ss-local --fast-open`
