---
layout: page
title: osx/lldb (español)
description: "El depurador de bajo nivel LLVM."
content_hash: f52f7fda12ac14b959c44fed99292e626ebfb10b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/lldb.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/lldb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lldb

El depurador de bajo nivel LLVM.
Más información: <https://lldb.llvm.org/man/lldb.html>.

- Depura un ejecutable:

`lldb "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejecutable</span>`"`

- Adjunta `lldb` a un proceso en ejecución con un PID dado:

`lldb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Espera a que se inicie un nuevo proceso con un nombre determinado y adjuntarlo al mismo:

`lldb -w -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_proceso</span>`"`
