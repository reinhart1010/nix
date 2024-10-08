---
layout: page
title: common/sv (English)
description: "Control a running runsv service."
content_hash: 2d5ac7c481228f924f774cbc6e1f7ac3612e3b51
last_modified_at: 2024-10-08
related_topics:
  - title: 中文 version
    url: /zh/common/sv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sv

Control a running runsv service.
More information: <https://manned.org/sv.8>.

- Start a service:

`sudo sv up `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/service</span>

- Stop a service:

`sudo sv down `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/service</span>

- Get service status:

`sudo sv status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/service</span>

- Reload a service:

`sudo sv reload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/service</span>

- Start a service, but only if it's not running and don't restart it if it stops:

`sudo sv once `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/service</span>
