---
layout: page
title: linux/unshare (English)
description: "Execute a command in new user-defined namespaces."
content_hash: 0f12fa2d818d0ddb114ba582c9b5723b442ccf55
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># unshare

Execute a command in new user-defined namespaces.
More information: <https://www.kernel.org/doc/html/latest/userspace-api/unshare.html>.

- Execute a command without sharing access to connected networks:

`unshare --net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Execute a command as a child process without sharing mounts, processes, or networks:

`unshare --mount --pid --net --fork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>
