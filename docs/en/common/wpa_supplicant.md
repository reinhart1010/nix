---
layout: page
title: common/wpa_supplicant (English)
description: "Manage protected wireless networks."
content_hash: 8b7f19e8ad9800227c06c0edf9c29db0ad49142e
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/wpa_supplicant.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wpa_supplicant

Manage protected wireless networks.
More information: <https://manned.org/wpa_supplicant.1>.

- Join a protected wireless network:

`wpa_supplicant -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wpa_supplicant_conf.conf</span>

- Join a protected wireless network and run it in a daemon:

`wpa_supplicant -B -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/wpa_supplicant_conf.conf</span>
