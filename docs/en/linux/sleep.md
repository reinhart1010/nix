---
layout: page
title: linux/sleep (English)
description: "Delay for a specified amount of time."
content_hash: d72044b75c0afb80562e7c673420f07c57ee7ba2
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/sleep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/sleep.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/sleep.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/sleep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sleep

Delay for a specified amount of time.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/sleep-invocation.html>.

- Delay in seconds:

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>

- Delay in [m]inutes. (Other units [d]ay, [h]our, [s]econd, [inf]inity can also be used):

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutes</span>`m`

- Delay for 1 [d]ay 3 [h]ours:

`sleep 1d 3h`

- Execute a specific command after 20 [m]inutes delay:

`sleep 20m && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
