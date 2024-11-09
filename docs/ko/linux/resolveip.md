---
layout: page
title: linux/resolveip (한국어)
description: "호스트명을 IP 주소로, IP 주소를 호스트명으로 변환."
content_hash: 9d96948fbb63de1b67b790938b58c1b311c0066b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/resolveip.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/resolveip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># resolveip

호스트명을 IP 주소로, IP 주소를 호스트명으로 변환.
더 많은 정보: <https://mariadb.com/kb/en/resolveip/>.

- 호스트명을 IP 주소로 변환:

`resolveip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>

- IP 주소를 호스트명으로 변환:

`resolveip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>

- 조용한 모드. 출력량을 줄임:

`resolveip --silent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>
