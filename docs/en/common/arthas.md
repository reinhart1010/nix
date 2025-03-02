---
layout: page
title: common/arthas (English)
description: "Java diagnostic tool."
content_hash: 720e6571d0faa82127f18a7b875db2fef69e6202
last_modified_at: 2025-03-02
related_topics:
  - title: 中文 version
    url: /zh/common/arthas.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arthas

Java diagnostic tool.
See also: `arthas-watch`, `arthas-trace`.
More information: <https://arthas.aliyun.com/en/>.

- Start Arthas:

`java -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/arthas-boot.jar</span>

- Reconnect Arthas (default port used by Arthas is 3658):

`telnet localhost `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>

- Exit the current Arthas client without affecting other clients. equals `exit`、`logout`、`q` command:

`exit|quit|logout|q`

- Terminate the Arthas server, all the Arthas clients connecting to this server will be disconnected:

`stop`
