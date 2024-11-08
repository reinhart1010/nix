---
layout: page
title: linux/bpftool (한국어)
description: "eBPF 프로그램 및 맵을 간단하게 검사하고 조작."
content_hash: cb738e21a5cfd50634e3f5c185082a6ae479bb4f
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/bpftool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/bpftool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bpftool

eBPF 프로그램 및 맵을 간단하게 검사하고 조작.
`prog`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://manned.org/bpftool>.

- 로드된 `eBPF` 프로그램 정보 나열:

`bpftool prog list`

- 커널 네트워킹 하위 시스템의 `eBPF` 프로그램 연결 나열:

`bpftool net list`

- 모든 활성 링크 나열:

`bpftool link list`

- 시스템의 모든 `raw_tracepoint`, `tracepoint`, `kprobe` 연결 나열:

`bpftool perf list`

- `BPF Type Format (BTF)` 데이터 나열:

`bpftool btf list`

- 로드된 맵 정보 나열:

`bpftool map list`

- 네트워크 장치 "eth0"의 지원하는 `eBPF` 기능 검사:

`bpftool feature probe dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 파일에서 배치 모드로 명령 실행:

`bpftool batch file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내_파일</span>
