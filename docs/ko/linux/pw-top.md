---
layout: page
title: linux/pw-top (한국어)
description: "실시간으로 PipeWire 노드 및 장치 통계를 확인."
content_hash: 483f449479c8a493c515f23ffc66a1e3ca61c4ea
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/pw-top.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-top.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-top.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-top

실시간으로 PipeWire 노드 및 장치 통계를 확인.
같이 보기: `pipewire`, `pw-dump`, `pw-cli`, `pw-profiler`.
더 많은 정보: <https://docs.pipewire.org/page_man_pw-top_1.html>.

- PipeWire 노드와 장치의 대화형 뷰 표시:

`pw-top`

- 원격 인스턴스 모니터링:

`pw-top --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>

- 대화형 모드 대신 주기적으로 정보 출력:

`pw-top --batch-mode`

- 특정 횟수만큼 주기적으로 정보 출력:

`pw-top --batch-mode --iterations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
