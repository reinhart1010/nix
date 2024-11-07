---
layout: page
title: common/license (한국어)
description: "오픈 소스 프로젝트를 위한 라이선스 파일 생성."
content_hash: cdd08a2a515805a7d1325a872225be13b6d9e95a
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/license.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/license.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># license

오픈 소스 프로젝트를 위한 라이선스 파일 생성.
더 많은 정보: <https://nishanths.github.io/license>.

- 기본값(자동 감지된 작성자 이름 및 현재 연도)을 사용하여 `stdout`에 라이선스 출력:

`license `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라이선스_이름</span>

- 라이선스를 생성하고 파일에 저장:

`license -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라이선스_이름</span>

- 사용 가능한 모든 라이선스 나열:

`license ls`

- 사용자 정의 작성자 이름과 연도로 라이선스 생성:

`license --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작성자</span>` --year `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출시_연도</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라이선스_이름</span>
