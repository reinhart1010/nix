---
layout: page
title: common/lldb (español)
description: "El depurador LLVM de bajo nivel."
content_hash: c58e838ec59e316f2627d1b9db8ce38b94a0a185
last_modified_at: 2024-12-30
related_topics:
  - title: English version
    url: /en/common/lldb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/lldb.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/lldb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lldb

El depurador LLVM de bajo nivel.
Más información: <https://lldb.llvm.org>.

- Depura un ejecutable:

`lldb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejecutable</span>

- Asocia `lldb` a un proceso de ejecución con un PID dado:

`lldb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Espera un nuevo proceso con un nombre dado para ejecutarse y asociarse al mismo:

`lldb -w -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_proceso</span>
