---
layout: page
title: common/kubectl-run (한국어)
description: "Kubernetes에서 파드를 실행. 일부 K8S 버전에서 경고 메시지를 피하기 위해 파드 생성기를 지정."
content_hash: d091a45187c0ba0f449034e0e2b286dedca39e5f
last_modified_at: 2024-11-01
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl-run.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/kubectl-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl run

Kubernetes에서 파드를 실행. 일부 K8S 버전에서 경고 메시지를 피하기 위해 파드 생성기를 지정.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run>.

- nginx 파드를 실행하고 포트 80을 노출:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx-dev</span>` --image=nginx --port 80`

- TEST_VAR 환경 변수를 설정하여 nginx 파드 실행:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx-dev</span>` --image=nginx --env="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TEST_VAR</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testing</span>`"`

- nginx 컨테이너를 생성하기 위해 수행될 API 호출을 표시:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx-dev</span>` --image=nginx --dry-run=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|server|client</span>

- Ubuntu 파드를 대화형으로 실행, 재시작하지 않으며 종료 시 제거:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">temp-ubuntu</span>` --image=ubuntu:22.04 --restart=Never --rm -- /bin/bash`

- 기본 명령을 echo로 변경하고 사용자 정의 인수를 지정하여 Ubuntu 파드 실행:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">temp-ubuntu</span>` --image=ubuntu:22.04 --command -- echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>
