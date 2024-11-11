---
layout: page
title: linux/getent (한국어)
description: "Name Service Switch 라이브러리에서 항목을 가져옵니다."
content_hash: d766c49add8fd13ed85d0ced71dfbfa2ebe2d64a
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/getent.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/getent.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># getent

Name Service Switch 라이브러리에서 항목을 가져옵니다.
더 많은 정보: <https://manned.org/getent>.

- 모든 그룹 나열:

`getent group`

- 그룹의 멤버 확인:

`getent group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>

- 모든 서비스 나열:

`getent services`

- UID로 사용자명 찾기:

`getent passwd 1000`

- 역방향 DNS 조회 수행:

`getent hosts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>
