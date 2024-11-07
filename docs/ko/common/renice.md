---
layout: page
title: common/renice (한국어)
description: "실행 중인 프로세스의 스케줄링 우선순위/친화도를 변경."
content_hash: eeaf2869b94f1acde7d25d66a06e9f65dec7d379
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/renice.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/renice.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/renice.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/renice.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># renice

실행 중인 프로세스의 스케줄링 우선순위/친화도를 변경.
친화도 값은 -20(프로세스에 가장 유리함)에서 19(프로세스에 가장 불리함)까지.
같이 보기: `nice`.
더 많은 정보: <https://manned.org/renice>.

- 실행 중인 [p]rocess의 우선순위를 증가/감소:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 특정 [u]ser가 소유한 모든 프로세스의 우선순위를 증가/감소:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-4</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|사용자</span>

- 프로세스 [g]roup에 속한 모든 프로세스의 우선순위를 증가/감소:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_그룹</span>
