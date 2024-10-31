---
layout: page
title: common/kubectl-logs (한국어)
description: "컨테이너의 로그를 조회하는 도구."
content_hash: 0b2d2a20a93e15fc61dfa3c664329162a1f91c27
last_modified_at: 2024-10-31
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl-logs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/kubectl-logs.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/kubectl-logs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kubectl-logs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kubectl logs

컨테이너의 로그를 조회하는 도구.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs>.

- 단일 컨테이너가 있는 파드의 로그 조회:

`kubectl logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>

- 특정 컨테이너의 로그 조회:

`kubectl logs --container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>

- 포드 내 모든 컨테이너의 로그 조회:

`kubectl logs --all-containers=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>

- 포드 로그 스트리밍:

`kubectl logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>

- `10s`, `5m` 또는 `1h`와 같은 상대 시간 이후의 포드 로그 조회:

`kubectl logs --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">상대_시간</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>

- 가장 최근의 10개의 포드 로그 조회:

`kubectl logs --tail=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>

- 특정 배포의 모든 포드 로그 조회:

`kubectl logs deployment/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배포_이름</span>
