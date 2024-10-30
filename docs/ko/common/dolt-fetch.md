---
layout: page
title: common/dolt-fetch (한국어)
description: "다른 저장소에서 객체와 참조를 다운로드."
content_hash: 66b73d57d27aed1beadee227fa24717b88b46876
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/dolt-fetch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dolt-fetch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dolt fetch

다른 저장소에서 객체와 참조를 다운로드.
더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-fetch>.

- 기본 원격 업스트림 저장소(origin)에서 최신 변경 사항을 가져옴:

`dolt fetch`

- 특정 원격 업스트림 저장소에서 최신 변경 사항을 가져옴:

`dolt fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>

- 원격의 현재 상태로 브랜치를 업데이트하고, 충돌하는 기록을 덮어씀:

`dolt fetch -f`
