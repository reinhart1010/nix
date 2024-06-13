---
layout: page
title: linux/sockstat (Nederlands)
description: "Toon open Internet- of UNIX-domeinsockets."
content_hash: e4c4cd6b7a412138a7fc92a5d12fccd4cb4717e1
last_modified_at: 2024-06-13
related_topics:
  - title: English version
    url: /en/linux/sockstat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sockstat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sockstat

Toon open Internet- of UNIX-domeinsockets.
Bekijk ook: `netstat`.
Meer informatie: <https://manned.org/sockstat>.

- Toon informatie voor IPv4- en IPv6-sockets voor zowel luister- als verbonden sockets:

`sockstat`

- Toon informatie voor IPv[4]/IPv[6] sockets die [l]uisteren op specifieke [p]oorten met een specifiek p[R]otocol:

`sockstat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>` -l -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|sctp|divert</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort1,poort2...</span>

- Toon ook [c]onnected sockets en [u]nix-sockets:

`sockstat -cu`

- Toon alleen sockets van het opgegeven `pid` of proces:

`sockstat -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid|proces</span>

- Toon alleen sockets van de opgegeven `uid` of gebruiker:

`sockstat -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|gebruiker</span>

- Toon alleen sockets van de opgegeven `gid` of groep:

`sockstat -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gid|groep</span>
