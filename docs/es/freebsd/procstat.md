---
layout: page
title: freebsd/procstat (español)
description: "Muestra información detallada sobre los procesos en FreeBSD."
content_hash: 4c5aff9553533fbebd5296f710c2920d264f5ac9
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/freebsd/procstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# procstat

Muestra información detallada sobre los procesos en FreeBSD.
Más información: <https://man.freebsd.org/cgi/man.cgi?query=procstat>.

- Muestra los descriptores de archivo de un proceso específico:

`procstat fds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Muestra las asignaciones de memoria virtual de un proceso:

`procstat vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Muestra los argumentos de un proceso:

`procstat arguments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Muestra los límites de recursos de un proceso:

`procstat rlimit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
