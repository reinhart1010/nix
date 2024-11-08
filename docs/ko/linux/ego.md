---
layout: page
title: linux/ego (한국어)
description: "Funtoo의 공식 시스템 성격 관리 도구."
content_hash: a3df9d21aa07c4e27e5e20916f5906432d73e4b4
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/ego.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ego.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ego

Funtoo의 공식 시스템 성격 관리 도구.
더 많은 정보: <https://funtoo-ego.readthedocs.io/en/develop/>.

- Portage 트리 동기화:

`ego sync`

- 부트로더 구성 업데이트:

`ego boot update`

- 이름으로 Funtoo 위키 페이지 읽기:

`ego doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">위키_페이지</span>

- 현재 프로필 출력:

`ego profile show`

- 믹스인 활성화/비활성화:

`ego profile mix-in +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gnome</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kde-plasma-5</span>

- 특정 패키지와 관련된 Funtoo 버그 쿼리:

`ego query bug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
