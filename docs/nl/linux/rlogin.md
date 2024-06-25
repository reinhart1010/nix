---
layout: page
title: linux/rlogin (Nederlands)
description: "Log in op een externe host."
content_hash: 9197af2dbe2b971bb1aa9e786ffb3c10de4f271f
last_modified_at: 2024-06-25
related_topics:
  - title: English version
    url: /en/linux/rlogin.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rlogin.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rlogin

Log in op een externe host.
Meer informatie: <https://www.gnu.org/software/inetutils/manual/html_node/rlogin-invocation.html>.

- Log in op een externe host:

`rlogin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- Log in op een externe host met een specifieke gebruikersnaam:

`rlogin -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>
