---
layout: page
title: linux/bpftrace (português (Brasil))
description: "Linguagem de análise de alto nível para eBPF Linux."
content_hash: 9de21519bbd23b680112495f9cbc355c15e0540a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/bpftrace.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bpftrace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bpftrace

Linguagem de análise de alto nível para eBPF Linux.
Mais informações: <https://github.com/iovisor/bpftrace>.

- Verifique a versão do bpftrace:

`bpftrace -V`

- Lista todos os probes:

`sudo bpftrace -l`

- Rode um programa de uma linha (e.g. número de syscalls por programa):

`sudo bpftrace -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }</span>`'`

- Rode um programa de um arquivo:

`sudo bpftrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo</span>

- Analise um programa por PID:

`sudo bpftrace -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracepoint:raw_syscalls:sys_enter /pid == 123/ { @[comm] = count(); }</span>`'`

- Mostre o resultado do programa em eBPF, sem rodar ele:

`sudo bpftrace -d -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa_de_uma_linha</span>`'`
