---
layout: page
title: freebsd/procstat (English)
description: "Display detailed information about processes in FreeBSD."
content_hash: a6837c7dc946acc9c2d1e01ad56fd63c9b636bca
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/freebsd/procstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# procstat

Display detailed information about processes in FreeBSD.
More information: <https://man.freebsd.org/cgi/man.cgi?query=procstat>.

- Display file descriptors of a specific process:

`procstat fds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Show virtual memory mappings of a process:

`procstat vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Display process arguments:

`procstat arguments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Show resource limits of a process:

`procstat rlimit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
