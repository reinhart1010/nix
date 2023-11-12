---
layout: page
title: sunos/prctl (English)
description: "Get or set the resource controls of running processes, tasks, and projects."
content_hash: ed4897e13a683eefa53bd6e0e8e5c9c390384935
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/sunos/prctl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prctl.html
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

Get or set the resource controls of running processes, tasks, and projects.
More information: <https://www.unix.com/man-page/sunos/1/prctl>.

- Examine process limits and permissions:

`prctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Examine process limits and permissions in machine parsable format:

`prctl -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Get specific limit for a running process:

`prctl -n process.max-file-descriptor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
