---
layout: page
title: common/stern (한국어)
description: "Kubernetes의 여러 팟 및 컨테이너 로그를 동시에 확인."
content_hash: 19c07e862ac4efbdf7340faeba29abf308e3cd34
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/stern.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/stern.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stern

Kubernetes의 여러 팟 및 컨테이너 로그를 동시에 확인.
더 많은 정보: <https://github.com/stern/stern>.

- 현재 네임스페이스 내의 모든 팟 로그 확인:

`stern .`

- 특정 상태의 모든 팟 로그 확인:

`stern . --container-state `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">running|waiting|terminated</span>

- 주어진 정규 표현식과 일치하는 모든 팟 로그 확인:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">팟_쿼리</span>

- 모든 네임스페이스에서 일치하는 팟 로그 확인:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">팟_쿼리</span>` --all-namespaces`

- 15분 전부터 일치하는 팟 로그 확인:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">팟_쿼리</span>` --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15m</span>

- 특정 레이블이 있는 일치하는 팟 로그 확인:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">팟_쿼리</span>` --selector `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release=canary</span>
