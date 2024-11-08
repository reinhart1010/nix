---
layout: page
title: linux/bully (한국어)
description: "무선 액세스 포인트의 WPS 핀을 무차별 대입으로 알아냅니다."
content_hash: 5697e81692ecec1c9263f3a1215da9c649e4e202
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/bully.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/bully.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bully

무선 액세스 포인트의 WPS 핀을 무차별 대입으로 알아냅니다.
`bully`를 사용하기 전에 필요한 정보를 `airmon-ng` 및 `airodump-ng`로 수집해야 합니다.
더 많은 정보: <https://salsa.debian.org/pkg-security-team/bully>.

- 비밀번호 크랙:

`bully --bssid "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">맥</span>`" --channel "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">채널</span>`" --bruteforce "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>`"`

- 도움말 표시:

`bully --help`
