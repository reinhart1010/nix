---
layout: page
title: common/lldb (Nederlands)
description: "De LLVM Low-Level Debugger."
content_hash: 0a5ef6484464f554dbd72c0a22223fe85e527b36
last_modified_at: 2024-08-21
related_topics:
  - title: English version
    url: /en/common/lldb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lldb

De LLVM Low-Level Debugger.
Meer informatie: <https://lldb.llvm.org>.

- Debug een uitvoerbaar bestand:

`lldb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoerbaar_bestand</span>

- Koppel `lldb` aan een draaiend proces met een gegeven PID:

`lldb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Wacht op de start van een nieuw proces met een gegeven naam en koppel eraan:

`lldb -w -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_naam</span>
