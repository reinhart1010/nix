---
layout: page
title: common/sk (한국어)
description: "Rust로 작성된 퍼지 파인더."
content_hash: e4c219aaed0bf5c4ed8a334b7b748d963a88e483
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sk

Rust로 작성된 퍼지 파인더.
`fzf`와 유사.
더 많은 정보: <https://github.com/lotabout/skim>.

- 지정된 디렉터리 내 모든 파일에서 `skim` 시작:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` -type f | sk`

- 실행 중인 프로세스에 대해 `skim` 시작:

`ps aux | sk`

- 지정된 쿼리로 `skim` 시작:

`sk --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>`"`

- `Shift + Tab`으로 여러 파일 선택 후 파일에 쓰기:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` -type f | sk --multi > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
