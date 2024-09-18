---
layout: page
title: linux/apache2ctl (English)
description: "Administrate the Apache HTTP web server."
content_hash: c07a7d4681f7efe31432af200c1a7fd8c71deb99
last_modified_at: 2024-09-18
related_topics:
  - title: Deutsch version
    url: /de/linux/apache2ctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apache2ctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apache2ctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apache2ctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apache2ctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apache2ctl

Administrate the Apache HTTP web server.
This command comes with Debian based OSes, for RHEL based ones see `httpd`.
More information: <https://manned.org/apache2ctl.8>.

- Start the Apache daemon. Throw a message if it is already running:

`sudo apache2ctl start`

- Stop the Apache daemon:

`sudo apache2ctl stop`

- Restart the Apache daemon:

`sudo apache2ctl restart`

- Test syntax of the configuration file:

`sudo apache2ctl -t`

- List loaded modules:

`sudo apache2ctl -M`
