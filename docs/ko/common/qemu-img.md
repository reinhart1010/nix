---
layout: page
title: common/qemu-img (한국어)
description: "Quick Emulator 가상 HDD 이미지를 생성 및 조작."
content_hash: 2c2722ab67a63b4c7222f1a9a3adf233c1ae6cf6
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/qemu-img.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qemu-img

Quick Emulator 가상 HDD 이미지를 생성 및 조작.
더 많은 정보: <https://qemu.readthedocs.io/en/master/tools/qemu-img.html>.

- 특정 크기(기가바이트 단위)로 디스크 이미지 생성:

`qemu-img create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름.img</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기가바이트</span>`G`

- 디스크 이미지 정보 표시:

`qemu-img info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름.img</span>

- 이미지 크기 증가 또는 감소:

`qemu-img resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름.img</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기가바이트</span>`G`

- 지정된 디스크 이미지의 각 섹터 할당 상태 덤프:

`qemu-img map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름.img</span>

- VMware .vmdk 디스크 이미지를 KVM .qcow2 디스크 이미지로 변환:

`qemu-img convert -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vmdk</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qcow2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일/foo.vmdk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일/foo.qcow2</span>
