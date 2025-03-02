---
layout: page
title: common/mkfifo (English)
description: "Make FIFOs (named pipes)."
content_hash: 0dd6c1e1b9b676d68fa1fdf4a1e87eef92c710cb
last_modified_at: 2025-03-02
related_topics:
  - title: bosanski version
    url: /bs/common/mkfifo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mkfifo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/mkfifo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/mkfifo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfifo

Make FIFOs (named pipes).
More information: <https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html>.

- Create a named pipe at a given path:

`mkfifo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pipe</span>

- Send data through a named pipe and send the command to the background:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pipe</span>` &`

- Receive data through a named pipe:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pipe</span>

- Share your terminal session in real-time:

`mkfifo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pipe</span>`; script -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pipe</span>
