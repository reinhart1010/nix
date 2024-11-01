---
layout: page
title: common/tlmgr-info (한국어)
description: "TeX Live 패키지에 대한 정보 표시."
content_hash: 8b8742e1c76e15f1e42a2f27dab46135dbe5c70e
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/tlmgr-info.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-info.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr info

TeX Live 패키지에 대한 정보 표시.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 설치된 패키지에 `i`를 접두사로 붙여 모든 사용 가능한 TeX Live 패키지 나열:

`tlmgr info`

- 모든 사용 가능한 컬렉션 나열:

`tlmgr info collections`

- 모든 사용 가능한 스키마 나열:

`tlmgr info scheme`

- 특정 패키지에 대한 정보 표시:

`tlmgr info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 패키지에 포함된 모든 파일 나열:

`tlmgr info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --list`

- 설치된 모든 패키지 나열:

`tlmgr info --only-installed`

- 패키지에 대한 특정 정보만 표시:

`tlmgr info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --data "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">category</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">installed</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depends</span>`,..."`

- 모든 사용 가능한 패키지를 JSON 인코딩된 배열로 출력:

`tlmgr info --json`
