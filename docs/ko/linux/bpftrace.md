---
layout: page
title: linux/bpftrace (한국어)
description: "Linux eBPF를 위한 고급 추적 언어."
content_hash: e1bb821e4d56b05ce98af16022f6745f2584cf35
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/bpftrace.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/bpftrace.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bpftrace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bpftrace

Linux eBPF를 위한 고급 추적 언어.
더 많은 정보: <https://github.com/iovisor/bpftrace>.

- bpftrace 버전 표시:

`bpftrace -V`

- 사용 가능한 모든 프로브 나열:

`sudo bpftrace -l`

- 원라이너 프로그램 실행 (예: 프로그램별 시스템 호출 수):

`sudo bpftrace -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }</span>`'`

- 파일에서 프로그램 실행:

`sudo bpftrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- PID로 프로그램 추적:

`sudo bpftrace -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracepoint:raw_syscalls:sys_enter /pid == 123/ { @[comm] = count(); }</span>`'`

- 드라이런을 수행하고 eBPF 형식으로 출력 표시:

`sudo bpftrace -d -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">한_줄_프로그램</span>`'`
