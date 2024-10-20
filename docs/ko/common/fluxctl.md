---
layout: page
title: common/fluxctl (한국어)
description: "Flux v1용 명령줄 도구."
content_hash: 77baada7ddfd7e4c67215d137d21c636b086f9d8
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fluxctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fluxctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fluxctl

Flux v1용 명령줄 도구.
더 많은 정보: <https://fluxcd.io/legacy/flux/references/fluxctl>.

- 특정 네임스페이스의 클러스터에서 현재 실행 중인 워크로드를 나열:

`fluxctl --k8s-fwd-ns=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>` list-workloads`

- 배포 및 사용 가능한 이미지 표시:

`fluxctl list-images`

- 클러스터를 Git 저장소와 동기화:

`fluxctl sync`

- 워크로드에 대한 자동 배포를 활성화:

`fluxctl automate`
