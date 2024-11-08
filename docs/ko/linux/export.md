---
layout: page
title: linux/export (한국어)
description: "셸 변수를 하위 프로세스로 내보냅니다."
content_hash: dd370fe09f2537e2549546bde87e1f2e8ab905a7
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/export.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/export.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/export.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/export.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># export

셸 변수를 하위 프로세스로 내보냅니다.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- 환경 변수를 설정:

`export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 환경 변수를 해제:

`export -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>

- 함수를 하위 프로세스로 내보내기:

`export -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">함수_이름</span>

- 환경 변수 `PATH`에 경로명 추가:

`export PATH=$PATH:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/추가</span>

- 셸 명령 형태로 활성화된 내보낸 변수 목록 표시:

`export -p`
