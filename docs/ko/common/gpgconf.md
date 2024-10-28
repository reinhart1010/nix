---
layout: page
title: common/gpgconf (한국어)
description: ".gnupg 홈 디렉터리를 수정."
content_hash: 1d8bedf3bb4db913fa8fba0480be3fa3a219d5b7
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/common/gpgconf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gpgconf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gpgconf

.gnupg 홈 디렉터리를 수정.
더 많은 정보: <https://www.gnupg.org/documentation/manuals/gnupg/gpgconf.html>.

- 모든 컴포넌트 나열:

`gpgconf --list-components`

- gpgconf가 사용하는 디렉토리를 나열:

`gpgconf --list-dirs`

- 컴포넌트의 모든 옵션을 나열:

`gpgconf --list-options `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컴포넌트</span>

- 프로그램을 나열하고 실행 가능한지 테스트:

`gpgconf --check-programs`

- 컴포넌트 리로드:

`gpgconf --reload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컴포넌트</span>
