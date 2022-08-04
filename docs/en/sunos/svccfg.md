---
layout: page
title: sunos/svccfg (English)
description: "Import, export, and modify service configurations."
content_hash: 08c7dd9fbc58aa7502800d56cc1cdc4cebf7ef4f
---
# svccfg

Import, export, and modify service configurations.
More information: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Validate configuration file:

`svccfg validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smf.xml</span>

- Export service configurations to file:

`svccfg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servicename</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smf.xml</span>

- Import/update service configurations from file:

`svccfg import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smf.xml</span>
