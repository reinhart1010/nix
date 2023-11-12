---
layout: page
title: common/sv (English)
description: "Control a running runsv service."
content_hash: 341f4f695dcb9b5a2f96a3207f95d6a86f8f9266
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/sv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sv

Control a running runsv service.
More information: <https://manpages.ubuntu.com/manpages/latest/man8/sv.8.html>.

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
