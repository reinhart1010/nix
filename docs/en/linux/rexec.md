---
layout: page
title: linux/rexec (English)
description: "Execute a command on a remote host."
content_hash: 5c90c1a07b37f1679ae25754d02ea13be6264c07
last_modified_at: 2023-11-11
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rexec

Execute a command on a remote host.
Note: Use `rexec` with caution, as it transmits data in plain text. Consider secure alternatives like `ssh` for encrypted communication.
More information: <https://www.gnu.org/software/inetutils/manual/html_node/rexec-invocation.html>.

- Execute a command on a remote [h]ost:

`rexec -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- Specify the remote [u]sername on a remote [h]ost:

`rexec -username=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps aux</span>

- Redirect `stdin` from `/dev/null` on a remote [h]ost:

`rexec --no-err -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- Specify the remote [P]ort on a remote [h]ost:

`rexec -P=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>` -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>
