---
layout: page
title: common/hostapd (한국어)
description: "무선 인터페이스를 사용하여 액세스 포인트를 시작."
content_hash: 0c9d5f7cf11c40222e7186667642b32518ba971c
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/hostapd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hostapd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hostapd

무선 인터페이스를 사용하여 액세스 포인트를 시작.
더 많은 정보: <https://w1.fi/hostapd/>.

- 액세스 포인트 시작:

`sudo hostapd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/hostapd.conf</span>

- 백그라운드로 분기하여, 액세스 포인트를 시작:

`sudo hostapd -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/hostapd.conf</span>
