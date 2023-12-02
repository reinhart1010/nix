---
layout: page
title: common/avo (한국어)
description: "Avo의 공식 인터넷 명령어 라인 인터페이스."
content_hash: 7f4cf9aa1c9b9693bffa574d751ed8f186648a18
last_modified_at: 2023-12-02
related_topics:
  - title: English version
    url: /en/common/avo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/avo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/avo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/avo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># avo

Avo의 공식 인터넷 명령어 라인 인터페이스.
더 많은 정보: <https://www.avo.app/docs/implementation/cli>.

- 현재 디렉터리에서 작업 공간 초기화:

`avo init`

- Avo 플랫폼에 로그인:

`avo login`

- 기존 Avo 지점으로 전환:

`avo checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 현재 경로에 대한 분석 래퍼 가져오기:

`avo pull`

- Avo 구현 상태 표시:

`avo status`

- Avo 파일의 Git 충돌 해결:

`avo conflict`

- 기본 웹 브라우저에서 현재 Avo 작업 공간을 공개:

`avo edit`

- 하위 명령에 대한 도움말 표시:

`avo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>` --help`
