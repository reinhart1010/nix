---
layout: page
title: common/tlmgr-shell (한국어)
description: "네이티브 TeX Live 관리자의 대화형 셸 시작."
content_hash: 13c8ae9681c36b2193bbb6eb3f83b9a11c122b65
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/tlmgr-shell.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-shell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr shell

네이티브 TeX Live 관리자의 대화형 셸 시작.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- `tlmgr`의 대화형 셸 시작:

`tlmgr shell`

- 대화형 셸에서 `tlmgr` 하위 명령 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수</span>

- 대화형 셸 종료:

`quit`

- 모든 TeX Live 변수 나열:

`get`

- 특정 TeX Live 변수의 값 가져오기:

`get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>

- 특정 TeX Live 변수의 값 설정:

`set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 대화형 셸 재시작:

`restart`

- 현재 프로토콜의 버전 표시:

`protocol`
