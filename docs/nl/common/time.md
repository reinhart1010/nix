---
layout: page
title: common/time (Nederlands)
description: "Meet hoe lang het uitvoeren van een commando duurt."
content_hash: 8d08352fc13609167b54e4050ab2f7ce090c06e7
last_modified_at: 2024-10-14
related_topics:
  - title: bosanski version
    url: /bs/common/time.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/time.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/time.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/time.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/time.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/time.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># time

Meet hoe lang het uitvoeren van een commando duurt.
Let op: `time` kan ofwel bestaan als een shell builtin, een op zichzelf staand programma of beide.
Meer informatie: <https://manned.org/time>.

- Voer het `commando` uit en print de tijdmetingen naar `stdout`::

`time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Maak een eenvoudige stopwatch (werkt alleen in Bash):

`time read`
