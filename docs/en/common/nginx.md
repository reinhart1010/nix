---
layout: page
title: common/nginx (English)
description: "Nginx web server."
content_hash: 68e1d1cd5ffc8e5f05c0956600312f0f03532d16
last_modified_at: 2024-01-25
related_topics:
  - title: Deutsch version
    url: /de/common/nginx.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nginx.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/nginx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nginx

Nginx web server.
More information: <https://nginx.org/en/>.

- Start server with the default configuration file:

`nginx`

- Start server with a custom configuration file:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_file</span>

- Start server with a prefix for all relative paths in the configuration file:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_file</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix/for/relative/paths</span>

- Test the configuration without affecting the running server:

`nginx -t`

- Reload the configuration by sending a signal with no downtime:

`nginx -s reload`
