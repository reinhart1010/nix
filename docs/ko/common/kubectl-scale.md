---
layout: page
title: common/kubectl-scale (한국어)
description: "배포, 레플리카 세트, 복제 컨트롤러 또는 스테이트풀 세트의 크기를 조정."
content_hash: 814830b55a1885e1e3804cafbaec8b76f2122791
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/kubectl-scale.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl scale

배포, 레플리카 세트, 복제 컨트롤러 또는 스테이트풀 세트의 크기를 조정.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#scale>.

- 레플리카 세트 크기 조정:

`kubectl scale --replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레플리카_수</span>` rs/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레플리카_이름</span>

- 파일로 식별된 리소스 크기 조정:

`kubectl scale --replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레플리카_수</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.yml</span>

- 현재 레플리카 수를 기준으로 배포 크기 조정:

`kubectl scale --current-replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">현재_레플리카_수</span>` --replicas=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레플리카_수</span>` deployment/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배포_이름</span>
