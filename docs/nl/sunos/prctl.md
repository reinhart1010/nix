---
layout: page
title: sunos/prctl (Nederlands)
description: "Lees of configureer de Get or set the resource controls of running processes, tasks, and projects."
content_hash: 9a14bd744b18eb0238161c6dd3d8cc183bb7ccf4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/prctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prctl.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prctl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prctl

Lees of configureer de Get or set the resource controls of running processes, tasks, and projects.
Meer informatie: <https://www.unix.com/man-page/sunos/1/prctl>.

- Uitlezen van de process limits en rechten:

`prctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Uitlezen van de process limits en rechten in een geformatteerde layout:

`prctl -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Uitlezen van het max file descripter van een lopend proces:

`prctl -n process.max-file-descriptor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>
