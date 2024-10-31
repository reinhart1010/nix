---
layout: page
title: common/kubectl-rollout (한국어)
description: "Kubernetes 리소스(배포, 데몬셋, 스테이트풀셋)의 롤아웃 관리."
content_hash: eacdcabf74c843164a208092029a4514c7b4de0f
last_modified_at: 2024-10-31
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl-rollout.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/kubectl-rollout.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kubectl-rollout.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kubectl rollout

Kubernetes 리소스(배포, 데몬셋, 스테이트풀셋)의 롤아웃 관리.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#rollout>.

- 리소스의 롤링 재시작 시작:

`kubectl rollout restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_유형</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_이름</span>

- 리소스의 롤링 업데이트 상태 보기:

`kubectl rollout status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_유형</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_이름</span>

- 리소스를 이전 리비전으로 롤백:

`kubectl rollout undo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_유형</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_이름</span>

- 리소스의 롤아웃 기록 보기:

`kubectl rollout history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_유형</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_이름</span>
