---
layout: page
title: common/unset (한국어)
description: "셸 변수 또는 함수를 제거."
content_hash: 25af158bde1c3d98573bf88cd0026a1bda987ecf
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/unset.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/unset.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unset

셸 변수 또는 함수를 제거.
더 많은 정보: <https://manned.org/unset>.

- 변수 `foo`를 제거하거나, 변수가 존재하지 않을 경우 함수 `foo`를 제거:

`unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 변수 `foo`와 `bar` 제거:

`unset -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- 함수 `my_func` 제거:

`unset -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_func</span>
