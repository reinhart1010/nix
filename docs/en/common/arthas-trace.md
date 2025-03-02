---
layout: page
title: common/arthas-trace (English)
description: "Trace method invoke chain, and output the time cost for each node in the path."
content_hash: d0adbe74a043f781c7119af0e1156f12573d9a6a
last_modified_at: 2025-03-02
related_topics:
  - title: 中文 version
    url: /zh/common/arthas-trace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arthas-trace

Trace method invoke chain, and output the time cost for each node in the path.
See also: `arthas`, `arthas-watch`.
More information: <https://arthas.aliyun.com/en/doc/trace.html>.

- Trace method invoke chain:

`trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern</span>

- Trace method invoke chains and only display invoke information longer than 10 ms:

`trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern</span>` '#cost > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`'`

- Trace the invoke chain of multiple classes or multiple methods:

`trace -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern1|class-patter2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern1|method-pattern2|method-pattern3</span>

- Track method invoke chains, only display invoke information that exceeds 10 ms, and exit after 5 times:

`trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern</span>` '#cost > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`' -n 5`
