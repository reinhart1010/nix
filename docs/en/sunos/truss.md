---
layout: page
title: sunos/truss (English)
description: "Troubleshooting tool for tracing system calls."
content_hash: 18be4cc8559e9201f25f41ae1b379f6498b023e2
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/sunos/truss.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/sunos/truss.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/truss.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/truss.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/truss.html
    icon: bi bi-globe
tldri18n_status: 2
---
# truss

Troubleshooting tool for tracing system calls.
SunOS equivalent of strace.
More information: <https://www.unix.com/man-page/linux/1/truss>.

- Start tracing a program by executing it, following all child processes:

`truss -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Start tracing a specific process by its PID:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Start tracing a program by executing it, showing arguments and environment variables:

`truss -a -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Count time, calls, and errors for each system call and report a summary on program exit:

`truss -c -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Trace a process filtering output by system call:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_call_name</span>
