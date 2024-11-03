---
layout: page
title: common/krunvm (한국어)
description: "OCI 이미지를 사용하여 MicroVM을 생성."
content_hash: 18708c9e0eab40315be93d27e2ed0fdc51f2a0fa
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/krunvm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/krunvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# krunvm

OCI 이미지를 사용하여 MicroVM을 생성.
더 많은 정보: <https://github.com/containers/krunvm>.

- Fedora 기반 MicroVM 생성:

`krunvm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker.io/fedora</span>` --cpus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vCPU_수</span>` --mem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메모리_메가바이트</span>` --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`"`

- 특정 이미지 시작:

`krunvm start "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>`"`

- 이미지 나열:

`krunvm list`

- 특정 이미지 변경:

`krunvm changevm --cpus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vCPU_수</span>` --mem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메모리_메가바이트</span>` --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_VM_이름</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">현재_VM_이름</span>`"`

- 특정 이미지 삭제:

`krunvm delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>`"`
