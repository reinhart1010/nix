---
layout: page
title: linux/extrepo (한국어)
description: "외부 Debian 저장소 관리."
content_hash: 60e8f912d066f5d720c98f212e43cef50ae83e81
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/extrepo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/extrepo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># extrepo

외부 Debian 저장소 관리.
Debian에서 외부 저장소를 관리하는 데 사용됩니다.
더 많은 정보: <https://manned.org/extrepo.1p>.

- 특정 패키지 검색:

`extrepo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 저장소 활성화:

`sudo extrepo enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>

- 저장소 비활성화:

`sudo extrepo disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>

- 저장소 업데이트:

`sudo extrepo update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>
