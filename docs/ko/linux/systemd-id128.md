---
layout: page
title: linux/systemd-id128 (한국어)
description: "sd-128 식별자를 생성하고 출력."
content_hash: 6d8c2a8223d4c9fd7daff6002e73d6b8021fb314
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-id128.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-id128.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-id128

sd-128 식별자를 생성하고 출력.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-id128.html>.

- 새로운 랜덤 식별자 생성:

`systemd-id128 new`

- 현재 머신의 식별자 출력:

`systemd-id128 machine-id`

- 현재 부팅의 식별자 출력:

`systemd-id128 boot-id`

- 현재 서비스 호출의 식별자 출력 (systemd 서비스에서 사용 가능):

`systemd-id128 invocation-id`

- 새로운 랜덤 식별자를 생성하고 UUID 형식으로 출력 (하이픈으로 구분된 다섯 그룹의 숫자):

`systemd-id128 new --uuid`
