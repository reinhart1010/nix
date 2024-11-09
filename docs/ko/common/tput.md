---
layout: page
title: common/tput (한국어)
description: "터미널 설정 및 기능을 조회하고 수정."
content_hash: 6c79353fca9fb36907318ab0d385439879b72328
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tput.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tput.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tput.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tput.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tput

터미널 설정 및 기능을 조회하고 수정.
더 많은 정보: <https://manned.org/tput>.

- 커서를 특정 화면 위치로 이동:

`tput cup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">행</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열</span>

- 전경색(af) 또는 배경색(ab) 설정:

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">setaf|setab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ANSI_색상_코드</span>

- 컬럼 수, 라인 수, 또는 색상 수 표시:

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cols|lines|colors</span>

- 터미널 벨 울리기:

`tput bel`

- 모든 터미널 속성 초기화:

`tput sgr0`

- 자동 줄바꿈 활성화 또는 비활성화:

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smam|rmam</span>
