---
layout: page
title: common/cargo-metadata (한국어)
description: "현재 패키지의 작업공간 멤버와 해결된 종속성을 JSON으로 출력."
content_hash: f657c5294cc03c364af9e4169340564e5f663f79
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-metadata.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-metadata.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-metadata.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo metadata

현재 패키지의 작업공간 멤버와 해결된 종속성을 JSON으로 출력.
참고: 출력 형식은 Cargo의 향후 버전에서 변경될 수 있음.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-metadata.html>.

- 현재 패키지의 작업공간 멤버 및 해결된 종속성을 출력:

`cargo metadata`

- 작업공간 멤버만 출력하고 종속성을 가져오지 않음:

`cargo metadata --no-deps`

- 지정된 버전에 따라 특정 형식으로 메타데이터를 인쇄:

`cargo metadata --format-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 주어진 타겟 트리플에 대한 종속성만 포함하는 `resolve` 필드로 메타데이터를 출력 (참고: `packages` 배열에는 여전히 모든 대상에 대한 종속성이 포함됨):

`cargo metadata --filter-platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟_아키텍처_정보</span>
