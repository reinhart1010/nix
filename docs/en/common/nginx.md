---
layout: page
title: common/nginx (English)
description: "Nginx web server."
content_hash: 6f8426379aa40cf61eca3a06fd5712ec8874ca2f
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

- Start server with a custom configuration file:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_file</span>

- Start server with a prefix for all relative paths in the configuration file:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_file</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix/for/relative/paths</span>

- Test the configuration without affecting the running server:

`nginx -t`

- Reload the configuration by sending a signal with no downtime:

`nginx -s reload`
