---
layout: page
title: sunos/truss (Nederlands)
description: "Troubleshooting tool voor het traceren van system calls."
content_hash: 886635823ccdde004d7e8b2f00419d79465d1cb7
related_topics:
  - title: English version
    url: /en/sunos/truss.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/truss.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># truss

Troubleshooting tool voor het traceren van system calls.
SunOS equivalent van strace.
Meer informatie: <https://www.unix.com/man-page/linux/1/truss>.

- Start het traceren van een programma door het uit te voeren, en de tracering van alle child processes:

`truss -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Start het traceren van een specifiek proces aan de hand van het PID:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Start het traceren van een programma door het uit te voeren, en toont alle argumenent en omgevingsinstellingen:

`truss -a -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Telt tijd, oproepen, en fouten voor elke systeem call en geeft een oplijsting bij de beindiging van de applicatie:

`truss -c -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Traceert een process filter output via system call:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_call_name</span>
