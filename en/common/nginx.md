---
layout: page
title: common/nginx (English)
description: "Nginx web server."
content_hash: e25a5e5e49a31f37a6d19f121d6ac99a351e0f39
related_topics:
  - title: Türkçe version
    url: /tr/common/nginx.html
    icon: bi bi-globe
---
# nginx

Nginx web server.
More information: <https://nginx.org/en/>.

- Start server with the default config file:

`nginx`

- Start server with a custom config file:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config_file</span>

- Start server with a prefix for all relative paths in the config file:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config_file</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix/for/relative/paths</span>

- Test the configuration without affecting the running server:

`nginx -t`

- Reload the configuration by sending a signal with no downtime:

`nginx -s reload`
