---
layout: page
title: common/cmctl (한국어)
description: "클러스터 내부의 cert-manager 리소스를 관리."
content_hash: dfaab0576a5096bd257a6a75faca89e181748c9e
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/cmctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cmctl

클러스터 내부의 cert-manager 리소스를 관리.
인증서 서명 상태를 확인하고, 요청을 승인/거부하고, 새 인증서 요청을 발급.
더 많은 정보: <https://cert-manager.io/docs/usage/cmctl/>.

- cert-manager API가 준비되었는지 확인:

`cmctl check api`

- 인증서 상태를 확인:

`cmctl status certificate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인증서_이름</span>

- 기존 인증서를 기반으로 새 인증서 요청을 만듬:

`cmctl create certificaterequest my-cr --from-certificate-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert.yaml</span>

- 새 인증서 요청을 생성하고, 서명된 인증서를 가져오고, 최대 대기 시간을 설정:

`cmctl create certificaterequest my-cr --from-certificate-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert.yaml</span>` --fetch-certificate --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20m</span>
