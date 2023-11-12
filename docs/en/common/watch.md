---
layout: page
title: common/watch (English)
description: "Execute a program periodically, showing output fullscreen."
content_hash: 99837075a183ce7542d82d16ed74771042f9906f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# watch

Execute a program periodically, showing output fullscreen.
More information: <https://manned.org/watch>.

- Repeatedly run a command and show the result:

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Re-run a command every 60 seconds:

`watch -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Monitor the contents of a directory, highlighting differences as they appear:

`watch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- Repeatedly run a pipeline and show the result:

`watch '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_1</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_2</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_3</span>`'`
