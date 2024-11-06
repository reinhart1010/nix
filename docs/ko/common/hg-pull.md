---
layout: page
title: common/hg-pull (한국어)
description: "지정된 저장소에서 로컬 저장소로 변경 사항을 가져옵니다."
content_hash: cb91e3b6aea9a1d9f4f02be51ef63d272e5f3c0b
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hg-pull.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hg-pull.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hg pull

지정된 저장소에서 로컬 저장소로 변경 사항을 가져옵니다.
더 많은 정보: <https://www.mercurial-scm.org/doc/hg.1.html#pull>.

- "기본" 소스 경로에서 가져오기:

`hg pull`

- 지정된 소스 저장소에서 가져오기:

`hg pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_저장소</span>

- 로컬 저장소를 원격의 최신 상태로 업데이트:

`hg pull --update`

- 원격 저장소가 관련이 없는 경우에도 변경 사항 가져오기:

`hg pull --force`

- 특정 리비전 변경 세트를 지정하여 가져오기:

`hg pull --rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리비전</span>

- 특정 브랜치를 지정하여 가져오기:

`hg pull --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치</span>

- 특정 북마크를 지정하여 가져오기:

`hg pull --bookmark `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">북마크</span>
