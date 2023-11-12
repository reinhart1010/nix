---
layout: page
title: common/exec (English)
description: "Replace the current process with another process."
content_hash: f4d47395c2963337a3c54a954802bce6bf35e166
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/exec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exec

Replace the current process with another process.
More information: <https://linuxcommand.org/lc3_man_pages/exech.html>.

- Replace with the specified command using the current environment variables:

`exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command -with -flags</span>

- Replace with the specified command, clearing environment variables:

`exec -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command -with -flags</span>

- Replace with the specified command and login using the default shell:

`exec -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command -with -flags</span>

- Replace with the specified command and change the process name:

`exec -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command -with -flags</span>
