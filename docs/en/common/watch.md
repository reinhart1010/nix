---
layout: page
title: common/watch (English)
description: "Execute a program periodically and monitor the output in full-screen mode."
content_hash: e5288ca112db0747f880f0ba1c27dd16460b2270
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/watch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# watch

Execute a program periodically and monitor the output in full-screen mode.
More information: <https://manned.org/watch>.

- Repeatedly run a command and show the result:

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Re-run a command every 60 seconds:

`watch --interval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Monitor disk space, highlighting differences as they appear:

`watch --differences `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">df</span>

- Repeatedly run a pipeline and show the result:

`watch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_1</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_2</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_3</span>`"`

- Exit `watch` if the visible output changes:

`watch --chgexit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lsblk</span>

- Interpret terminal control characters:

`watch --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls --color=always</span>
