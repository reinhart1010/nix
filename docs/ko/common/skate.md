---
layout: page
title: common/skate (한국어)
description: "간단하고 강력한 키-값 저장소."
content_hash: 0a0fc063d6db51fd0898dc466110d9412ba30610
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/skate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/skate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># skate

간단하고 강력한 키-값 저장소.
더 많은 정보: <https://github.com/charmbracelet/skate>.

- 기본 데이터베이스에 키와 값을 저장:

`skate set "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 기본 데이터베이스에 저장된 키 표시:

`skate list`

- 기본 데이터베이스에서 키와 값 삭제:

`skate delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`"`

- 새로운 데이터베이스에 키와 값을 생성:

`skate set "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`"@"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 기본이 아닌 데이터베이스에 저장된 키 표시:

`skate list @"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>`"`

- 특정 데이터베이스에서 키와 값 삭제:

`skate delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`"@"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>`"`

- 사용 가능한 데이터베이스 표시:

`skate list-dbs`

- 로컬 데이터베이스 삭제 및 Charm Cloud에서 새 복사본 가져오기:

`skate reset @"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>`"`
