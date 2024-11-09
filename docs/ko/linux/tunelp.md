---
layout: page
title: linux/tunelp (한국어)
description: "병렬 포트 장치의 다양한 매개변수를 설정하여 문제 해결 또는 성능 향상을 위한 도구."
content_hash: 33e6e5a5f0a887abfeedb161044f75951cb8cc54
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/tunelp.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/tunelp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tunelp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tunelp

병렬 포트 장치의 다양한 매개변수를 설정하여 문제 해결 또는 성능 향상을 위한 도구.
`util-linux`의 일부.
더 많은 정보: <https://manned.org/tunelp>.

- 병렬 포트 장치의 [s]상태 확인:

`tunelp --status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/lp0</span>

- 주어진 병렬 포트 [r]재설정:

`tunelp --reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/lp0</span>

- 장치에 사용할 [i]RQ 지정, 각 IRQ는 인터럽트 라인을 나타냄:

`tunelp -i 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/lp0</span>

- 프린터에 문자를 출력하기 위해 주어진 횟수만큼 시도한 후, 지정된 시간만큼 [c]대기:

`tunelp --chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">횟수</span>` --time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간_센티초</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/lp0</span>

- 오류 발생 시 [a]중지 활성화 또는 비활성화 (기본적으로 비활성화됨):

`tunelp --abort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>
