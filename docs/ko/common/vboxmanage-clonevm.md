---
layout: page
title: common/vboxmanage-clonevm (한국어)
description: "기존 가상 머신(VM)의 복제본 생성."
content_hash: f49a2a00838f280ae915a76ea12956cd6c312980
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/vboxmanage-clonevm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vboxmanage-clonevm

기존 가상 머신(VM)의 복제본 생성.
더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-clonevm>.

- 지정된 VM 복제:

`VBoxManage clonevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>

- 새로운 VM에 대한 새 이름 지정:

`VBoxManage clonevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_vm_이름</span>

- 새 VM 구성 파일이 저장될 폴더 지정:

`VBoxManage clonevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>` --basefolder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- VirtualBox에 복제된 VM 등록:

`VBoxManage clonevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>` --register`
