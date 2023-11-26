---
layout: page
title: linux/rsh (English)
description: "Execute commands on a remote host."
content_hash: 5e7b1348ade94e280f1cc1469254e985a14224d7
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# rsh

Execute commands on a remote host.
More information: <https://www.gnu.org/software/inetutils/manual/html_node/rsh-invocation.html>.

- Execute a command on a remote host:

`rsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- Execute a command on a remote host with a specific username:

`rsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- Redirect `stdin` to `/dev/null` when executing a command on a remote host:

`rsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` --no-err `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>
