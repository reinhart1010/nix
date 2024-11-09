---
layout: page
title: linux/ifmetric (한국어)
description: "IPv4 경로 메트릭 조정 도구."
content_hash: 9c00095a622700c30c280ba336dcb63a5322c65d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ifmetric.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ifmetric.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ifmetric

IPv4 경로 메트릭 조정 도구.
더 많은 정보: <https://0pointer.de/lennart/projects/ifmetric/>.

- 특정 네트워크 인터페이스의 우선순위 설정 (높은 숫자는 낮은 우선순위를 나타냄):

`sudo ifmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 특정 네트워크 인터페이스의 우선순위 초기화:

`sudo ifmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
