---
layout: page
title: common/readonly (한국어)
description: "읽기 전용 셸 변수를 설정합니다."
content_hash: ab576b83c47028e1b995b84504558b6ab5236924
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/readonly.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/readonly.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># readonly

읽기 전용 셸 변수를 설정합니다.
더 많은 정보: <https://manned.org/readonly.1posix>.

- 읽기 전용 변수 설정:

`readonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수_이름</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 변수 읽기 전용으로 표시:

`readonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기존_변수</span>

- 모든 읽기 전용 변수의 이름과 값을 `stdout`에 [p]rint:

`readonly -p`
