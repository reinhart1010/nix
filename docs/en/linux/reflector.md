---
layout: page
title: linux/reflector (English)
description: "Arch script to fetch and sort mirrorlists."
content_hash: a04259223c65c5c59c2673c7b61ad46f9d464bcb
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/reflector.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reflector

Arch script to fetch and sort mirrorlists.
More information: <https://manned.org/reflector>.

- Get all mirrors, sort for download speed and save them:

`sudo reflector --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rate</span>` --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/pacman.d/mirrorlist</span>

- Only get German HTTPS mirrors:

`reflector --country `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Germany</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https</span>

- Only get the 10 recently sync'd mirrors:

`reflector --latest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Use a configuration file to fetch mirrors:

`sudo reflector @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/xdg/reflector/reflector.conf</span>
