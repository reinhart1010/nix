---
layout: page
title: common/lsof (English)
description: "Lists open files and the corresponding processes."
content_hash: 9435076ef3b36ada78110f05f9717c66b1744c57
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/lsof.html
    icon: bi bi-globe
---
# lsof

Lists open files and the corresponding processes.
Note: Root privileges (or sudo) is required to list files opened by others.
More information: <https://manned.org/lsof>.

- Find the processes that have a given file open:

`lsof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Find the process that opened a local internet port:

`lsof -i :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Only output the process ID (PID):

`lsof -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- List files opened by the given user:

`lsof -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- List files opened by the given command or process:

`lsof -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_or_command_name</span>

- List files opened by a specific process, given its PID:

`lsof -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- List open files in a directory:

`lsof +D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Find the process that is listening on a local IPv6 TCP port and don't convert network or port numbers:

`lsof -i6TCP:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` -sTCP:LISTEN -n -P`
