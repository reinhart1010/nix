---
layout: page
title: common/helm (한국어)
description: "Kubernetes 패키지 관리자."
content_hash: 4d5f8e9a416da615d1470d635064600826cc25ef
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/helm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/helm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/helm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/helm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# helm

Kubernetes 패키지 관리자.
`install`과 같은 하위 명령어에는 자체 사용법 문서가 있음.
더 많은 정보: <https://helm.sh/>.

- helm 차트 생성:

`helm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">차트_이름</span>

- 새로운 helm 레포지토리를 추가:

`helm repo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_이름</span>

- helm 레포지토리 나열:

`helm repo list`

- helm 레포지토리 업데이트:

`helm repo update`

- helm 레포지토리 삭제:

`helm repo remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_이름</span>

- helm 차트 설치:

`helm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">차트_이름</span>

- tar 아카이브로 helm 차트 다운로드:

`helm get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">차트_배포_이름</span>

- helm 종속성 업데이트:

`helm dependency update`
