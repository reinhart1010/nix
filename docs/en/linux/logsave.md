---
layout: page
title: linux/logsave (English)
description: "Save the output of a command in a logfile."
content_hash: 154170d5d553d739a183e30f8e1600d0c29f140a
related_topics:
  - title: Deutsch version
    url: /de/linux/logsave.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/logsave.html
    icon: bi bi-globe
---
# logsave

Save the output of a command in a logfile.
More information: <https://manned.org/logsave>.

- Execute command with specified argument(s) and save its output to log file:

`logsave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/logfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Take input from standard input and save it in a log file:

`logsave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logfile</span>` -`

- Append the output to a log file, instead of replacing its current contents:

`logsave -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Show verbose output:

`logsave -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
