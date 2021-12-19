---
layout: page
title: common/pgrep (English)
description: "Find or signal processes by name."
content_hash: f0e0b68511db392be2eae0ac746f5beced596c2b
---
# pgrep

Find or signal processes by name.
More information: <https://www.man7.org/linux/man-pages/man1/pkill.1.html>.

- Return PIDs of any running processes with a matching command string:

`pgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- Search for processes including their command-line options:

`pgrep --full "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parameter</span>`"`

- Search for processes run by a specific user:

`pgrep --euid root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>
