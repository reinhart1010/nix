---
layout: page
title: common/stdbuf (Nederlands)
description: "Voer een commando uit met aangepaste buffering operaties voor de standaard streams."
content_hash: f906cb5437e0f998dc798549ee85a7ffc8a84f23
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/stdbuf.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/stdbuf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/stdbuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stdbuf

Voer een commando uit met aangepaste buffering operaties voor de standaard streams.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html>.

- Verander de buffer grootte van `stdin` naar 512 KiB:

`stdbuf --input=512K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Verander de buffer van `stdout` naar lijn-buffering:

`stdbuf --output=L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Verander de buffer van `stderr` naar ongebufferd:

`stdbuf --error=0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>
