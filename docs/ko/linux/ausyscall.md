---
layout: page
title: linux/ausyscall (한국어)
description: "시스템 호출 이름과 번호를 매핑합니다."
content_hash: 248aed2f2323ac0a6dbe557386945aad32b19a44
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/ausyscall.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ausyscall.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ausyscall

시스템 호출 이름과 번호를 매핑합니다.
더 많은 정보: <https://manned.org/ausyscall>.

- 특정 시스템 호출의 번호 표시:

`ausyscall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>

- 특정 시스템 호출 번호의 이름 표시:

`ausyscall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시스템_호출_번호</span>

- 특정 아키텍처의 모든 시스템 호출 표시:

`ausyscall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아키텍처</span>` --dump`
