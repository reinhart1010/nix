---
layout: page
title: common/virt-clone (한국어)
description: "libvirt 가상 머신 복제."
content_hash: 310f71147853b14261f8fff3017b0c8e83ad97cb
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/virt-clone.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virt-clone

libvirt 가상 머신 복제.
더 많은 정보: <https://manned.org/virt-clone>.

- 가상 머신을 복제하고 새 이름, 저장 경로 및 MAC 주소를 자동으로 생성:

`virt-clone --original `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상머신_이름</span>` --auto-clone`

- 가상 머신을 복제하고 새 이름, 저장 경로 및 MAC 주소를 지정:

`virt-clone --original `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상머신_이름</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_가상머신_이름</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새_저장소</span>` --mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ff:ff:ff:ff:ff:ff|RANDOM</span>
