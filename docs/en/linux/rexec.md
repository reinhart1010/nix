---
layout: page
title: linux/rexec (English)
description: "Execute a command on a remote host."
content_hash: 726c724248e6a4a4869530f2dea8fba78ef75fdc
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# rexec

Execute a command on a remote host.
Note: Use `rexec` with caution, as it transmits data in plain text. Consider secure alternatives like SSH for encrypted communication.
More information: <https://www.gnu.org/software/inetutils/manual/html_node/rexec-invocation.html>.

- Execute a command on a remote [h]ost:

`rexec -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- Specify the remote [u]sername on a remote [h]ost:

`rexec -username=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps aux</span>

- Redirect `stdin` from `/dev/null` on a remote [h]ost:

`rexec --no-err -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- Specify the remote [P]ort on a remote [h]ost:

`rexec -P=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>` -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>
