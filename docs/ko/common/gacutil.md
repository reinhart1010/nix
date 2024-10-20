---
layout: page
title: common/gacutil (한국어)
description: "전역 어셈블리 캐시 (Global Assembly Cache, CAG) 관리 유틸리티."
content_hash: 0462b93673a17c3557add025f577701334a73b50
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/gacutil.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gacutil.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gacutil

전역 어셈블리 캐시 (Global Assembly Cache, CAG) 관리 유틸리티.
더 많은 정보: <https://manned.org/gacutil>.

- 지정된 어셈블리를 GAC에 설치:

`gacutil -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.dll</span>

- GAC에서 지정된 어셈블리를 제거:

`gacutil -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">어셈블리_표시_이름</span>

- GAC의 내용을 출력:

`gacutil -l`
