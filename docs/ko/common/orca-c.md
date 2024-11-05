---
layout: page
title: common/orca-c (한국어)
description: "ORCA 라이브 프로그래밍 환경의 C 포트."
content_hash: 0132ad79850b473a7460695d47f62d717206fcdd
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/orca-c.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/orca-c.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># orca-c

ORCA 라이브 프로그래밍 환경의 C 포트.
ORCA는 절차적 시퀀서를 생성하기 위한 난해한 프로그래밍 언어입니다.
더 많은 정보: <https://github.com/hundredrabbits/Orca-c>.

- 빈 작업 공간으로 ORCA 시작:

`orca-c`

- 특정 파일을 열며 ORCA 시작:

`orca-c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.orca</span>

- 특정 템포로 ORCA 시작 (기본값은 120):

`orca-c --bpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분당_비트수</span>

- 그리드 크기를 설정하여 ORCA 시작:

`orca-c --initial-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">행</span>

- 최대 실행 취소 단계 수를 설정하여 ORCA 시작 (기본값은 100):

`orca-c --undo-limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제한</span>

- ORCA 내부에서 메인 메뉴 표시:

`F1`

- ORCA 내부에서 모든 단축키 표시:

`?`

- ORCA 내부에서 모든 ORCA 연산자 표시:

`<Ctrl> + g`
