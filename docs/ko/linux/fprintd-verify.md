---
layout: page
title: linux/fprintd-verify (한국어)
description: "데이터베이스에 저장된 지문을 검증합니다."
content_hash: 579e62a74a46ebde3fb94f68d82f7ef767e5f833
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/fprintd-verify.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fprintd-verify.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fprintd-verify

데이터베이스에 저장된 지문을 검증합니다.
더 많은 정보: <https://manned.org/fprintd-verify>.

- 현재 사용자의 모든 저장된 지문 검증:

`fprintd-verify`

- 현재 사용자의 특정 지문 검증:

`fprintd-verify --finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|right-index-finger|right-middle-finger|right-ring-finger|right-little-finger</span>

- 특정 사용자의 지문 검증:

`fprint-verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 특정 사용자의 특정 지문 검증:

`fprintd-verify --finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">손가락_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 현재 사용자의 데이터베이스에 저장된 지문과 일치하지 않으면 프로세스 실패:

`fprint-verify --g-fatal-warnings`

- 도움말 표시:

`fprintd-verify --help`
