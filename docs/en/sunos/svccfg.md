---
layout: page
title: sunos/svccfg (English)
description: "Import, export, and modify service configurations."
content_hash: e2a8a39094bdabbd427a16db7cc8c7e39bdace48
last_modified_at: 2023-02-20
related_topics:
  - title: Nederlands version
    url: /nl/sunos/svccfg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svccfg.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svccfg.html
    icon: bi bi-globe
---
# svccfg

Import, export, and modify service configurations.
More information: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Validate configuration file:

`svccfg validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/smf_file.xml</span>

- Export service configurations to file:

`svccfg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servicename</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/smf_file.xml</span>

- Import/update service configurations from file:

`svccfg import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/smf_file.xml</span>
