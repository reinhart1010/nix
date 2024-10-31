---
layout: page
title: common/kubectl (한국어)
description: "Kubernetes 클러스터에서 명령을 실행하기 위한 명령줄 인터페이스."
content_hash: a74db9834cf9644bbbba52c3eb1f5842fc6bde44
last_modified_at: 2024-10-31
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/kubectl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/kubectl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/kubectl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kubectl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kubectl

Kubernetes 클러스터에서 명령을 실행하기 위한 명령줄 인터페이스.
`run`과 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/>.

- 리소스에 대한 정보를 자세히 나열:

`kubectl get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod|service|deployment|ingress|...</span>` -o wide`

- 지정된 포드에 'unhealthy' 레이블과 'true' 값을 추가:

`kubectl label pods `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` unhealthy=true`

- 다양한 유형의 모든 리소스 나열:

`kubectl get all`

- 노드 또는 포드의 리소스(CPU/메모리/스토리지) 사용량 표시:

`kubectl top `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod|node</span>

- 마스터 및 클러스터 서비스의 주소 출력:

`kubectl cluster-info`

- 특정 필드에 대한 설명 표시:

`kubectl explain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pods.spec.containers</span>

- 포드 또는 지정된 리소스의 컨테이너 로그 출력:

`kubectl logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>

- 기존 포드에서 명령 실행:

`kubectl exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls /</span>
