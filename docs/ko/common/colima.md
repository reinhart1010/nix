---
layout: page
title: common/colima (한국어)
description: "최소한의 설정으로 macOS 및 Linux용 컨테이너 런타임을 제공."
content_hash: a08f95ae1da3ab3bc4156d17ce7c4d20370ca895
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/colima.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/colima.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/colima.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># colima

최소한의 설정으로 macOS 및 Linux용 컨테이너 런타임을 제공.
더 많은 정보: <https://github.com/abiosoft/colima>.

- 백그라운드에서 데몬을 시작:

`colima start`

- 구성 파일을 생성하고 사용:

`colima start --edit`

- containerd 시작 및 설정 (`nerdctl`을 통해 containerd를 사용하려면 `nerdctl` 설치):

`colima start --runtime containerd`

- Kubernetes로 시작 (`kubectl`이 필요):

`colima start --kubernetes`

- CPU 수, RAM 메모리 및 디스크 공간(GiB 단위)을 사용자 정의:

`colima start --cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` --memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메모리</span>` --disk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장_공간</span>

- Colima를 통해 Docker 사용 (Docker가 필요함):

`colima start`

- 정보 및 상태와 함께 컨테이너를 나열:

`colima list`

- 런타임 상태 표시:

`colima status`
