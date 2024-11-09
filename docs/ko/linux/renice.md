---
layout: page
title: linux/renice (한국어)
description: "실행 중인 프로세스의 스케줄링 우선순위/니스값을 변경합니다."
content_hash: ccb5dc1ae1043a91fffdf995c3dc975812d16ac8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/renice.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/renice.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/renice.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># renice

실행 중인 프로세스의 스케줄링 우선순위/니스값을 변경합니다.
니스값은 -20(프로세스에 가장 유리)부터 19(프로세스에 가장 불리)까지의 범위를 가집니다.
같이 보기: `nice`.
더 많은 정보: <https://manned.org/renice>.

- 실행 중인 [p]프로세스의 절대 우선순위 설정:

`renice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+3</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 특정 [u]사용자가 소유한 모든 프로세스의 우선순위 증가/감소:

`renice --relative `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-4</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|사용자</span>

- 프로세스 [g]그룹에 속한 모든 프로세스의 우선순위 설정:

`renice --absolute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_그룹</span>
