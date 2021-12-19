---
layout: page
title: linux/apache2ctl (English)
description: "The CLI tool to administrate HTTP web server Apache."
content_hash: 77325d00382c53b33af5b8539707734425608fdf
related_topics:
  - title: Deutsch version
    url: /de/linux/apache2ctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apache2ctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apache2ctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apache2ctl.html
    icon: bi bi-globe
---
# apache2ctl

The CLI tool to administrate HTTP web server Apache.
This command comes with Debian based OSes, for RHEL based ones see `httpd`.
More information: <https://manpages.debian.org/latest/apache2/apache2ctl.8.en.html>.

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
