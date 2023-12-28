---
layout: page
title: linux/bpftrace (português (Brasil))
description: "Linguagem de análise de alto nível para eBPF Linux."
content_hash: f2553e711844324e407049eb1c8afe6a3e9207ce
last_modified_at: 2023-12-28
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

- Exibe a versão do bpftrace:

`bpftrace -V`

- Lista todos os probes:

`sudo bpftrace -l`

- Roda um programa de uma linha (e.g. número de syscalls por programa):

`sudo bpftrace -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }</span>`'`

- Roda um programa de um arquivo:

`sudo bpftrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo</span>

- Analisa um programa por PID:

`sudo bpftrace -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracepoint:raw_syscalls:sys_enter /pid == 123/ { @[comm] = count(); }</span>`'`

- Mostra o resultado do programa em eBPF, sem rodar ele:

`sudo bpftrace -d -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa_de_uma_linha</span>`'`
