---
layout: page
title: common/mysql_secure_installation (English)
description: "Set up MySQL to have better security."
content_hash: 182be03545f007ea7c9312fa5fdec54ef290dae6
last_modified_at: 2024-09-16
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mysql_secure_installation.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mysql_secure_installation

Set up MySQL to have better security.
More information: <https://dev.mysql.com/doc/refman/en/mysql-secure-installation.html>.

- Start an interactive setup:

`mysql_secure_installation`

- Use specific host and port:

`mysql_secure_installation --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Display help:

`mysql_secure_installation --help`
