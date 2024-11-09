---
layout: page
title: linux/macchanger (한국어)
description: "네트워크 인터페이스 MAC 주소를 조작하는 명령줄 유틸리티."
content_hash: 271b6b92e5ac74267dd4899322c6f333a43bd021
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/macchanger.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/macchanger.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># macchanger

네트워크 인터페이스 MAC 주소를 조작하는 명령줄 유틸리티.
더 많은 정보: <https://manned.org/macchanger>.

- 인터페이스의 현재 및 영구 MAC 주소 보기:

`macchanger --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 인터페이스를 임의의 MAC으로 설정:

`macchanger --random `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 인터페이스를 임의의 MAC 주소로 설정하고, [b]urned-[i]n-[a]ddress로 가장:

`macchanger --random --bia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 인터페이스를 특정 MAC 주소로 설정:

`macchanger --mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XX:XX:XX:XX:XX:XX</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 알려진 모든 공급업체의 식별자(MAC 주소의 처음 세 바이트) 출력:

`macchanger --list`

- 인터페이스를 영구 하드웨어 MAC 주소로 재설정:

`macchanger --permanent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>
