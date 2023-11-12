---
layout: page
title: sunos/svcadm (English)
description: "Manipulate service instances."
content_hash: 7bbb3fe3ebe4fdc5f12da90eceb515097cdf0072
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/sunos/svcadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcadm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svcadm

Manipulate service instances.
More information: <https://www.unix.com/man-page/linux/1m/svcadm>.

- Enable a service in the service database:

`svcadm enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Disable service:

`svcadm disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Restart a running service:

`svcadm restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Command service to re-read configuration files:

`svcadm refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Clear a service from maintenance state and command it to start:

`svcadm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>
