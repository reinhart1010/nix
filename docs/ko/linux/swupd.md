---
layout: page
title: linux/swupd (한국어)
description: "Clear Linux의 패키지 관리 도구."
content_hash: 307f10311b9e3a7e5568404de74d4783d41c1e83
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/swupd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/swupd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># swupd

Clear Linux의 패키지 관리 도구.
더 많은 정보: <https://www.clearlinux.org/clear-linux-documentation/guides/clear/swupd.html>.

- 최신 버전으로 업데이트:

`sudo swupd update`

- 현재 버전을 표시하고, 새 버전이 있는지 확인:

`swupd check-update`

- 설치된 번들 나열:

`swupd bundle-list`

- 원하는 패키지가 존재하는 번들 찾기:

`swupd search -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 새 번들 설치:

`sudo swupd bundle-add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번들</span>

- 번들 제거:

`sudo swupd bundle-remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번들</span>

- 손상되었거나 누락된 파일 수정:

`sudo swupd verify`
