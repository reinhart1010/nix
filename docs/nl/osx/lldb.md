---
layout: page
title: osx/lldb (Nederlands)
description: "De LLVM Low-Level Debugger."
content_hash: 640741a6c0b07a6e7164b9c759b1b7f6cca88949
last_modified_at: 2024-08-21
related_topics:
  - title: English version
    url: /en/osx/lldb.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/lldb.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/lldb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lldb

De LLVM Low-Level Debugger.
Meer informatie: <https://lldb.llvm.org/man/lldb.html>.

- Debug een uitvoerbaar bestand:

`lldb "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoerbaar_bestand</span>`"`

- Koppel `lldb` aan een draaiend proces met een gegeven PID:

`lldb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Wacht op de start van een nieuw proces met een gegeven naam en koppel eraan:

`lldb -w -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_naam</span>`"`
