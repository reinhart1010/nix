---
layout: page
title: common/stdbuf (Nederlands)
description: "Voer een commando uit met aangepaste buffering operaties voor de standaard streams."
content_hash: 11338af4cd6621dcdc5adf54fcceb17edf0b7dac
last_modified_at: 2024-06-29
related_topics:
  - title: English version
    url: /en/common/stdbuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stdbuf

Voer een commando uit met aangepaste buffering operaties voor de standaard streams.
Meer informatie: <https://www.gnu.org/software/coreutils/stdbuf>.

- Verander de buffer grootte van `stdin` naar 512 KiB:

`stdbuf --input=512K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Verander de buffer van `stdout` naar lijn-buffering:

`stdbuf --output=L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Verander de buffer van `stderr` naar ongebufferd:

`stdbuf --error=0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>
