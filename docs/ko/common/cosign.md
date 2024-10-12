---
layout: page
title: common/cosign (한국어)
description: "OCI 레지스트리의 컨테이너 서명, 검증 및 저장."
content_hash: 3e03c63d70dda3a70a0220d08f0100fcfbb48099
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/cosign.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cosign

OCI 레지스트리의 컨테이너 서명, 검증 및 저장.
더 많은 정보: <https://github.com/sigstore/cosign>.

- 키의 쌍을 생성:

`cosign generate-key-pair`

- 컨테이너에 서명하고 레지스트리에 서명을 저장:

`cosign sign -key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cosign.key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- Kubernetes 비밀에 저장된 키 쌍을 사용하여 컨테이너 이미지에 서명:

`cosign sign -key k8s://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- 로컬 키 쌍 파일로 blob에 서명:

`cosign sign-blob --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cosign.key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 공개 키에 대해 컨테이너를 확인:

`cosign verify -key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cosign.pub</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- Dockerfile의 공개 키로 이미지를 확인:

`cosign dockerfile verify -key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cosign.pub</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Dockerfile</span>

- Kubernetes 비밀에 저장된 공개 키로 이미지를 확인:

`cosign verify -key k8s://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- 컨테이너 이미지와 해당 서명을 복사:

`cosign copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/src:latest</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/dest:latest</span>
