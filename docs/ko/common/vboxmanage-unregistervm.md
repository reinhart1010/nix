---
layout: page
title: common/vboxmanage-unregistervm (한국어)
description: "가상 머신(VM)을 등록 해제."
content_hash: a3c28a5c9c0119c793a387f1cba586355a9b4578
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/vboxmanage-unregistervm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vboxmanage-unregistervm

가상 머신(VM)을 등록 해제.
더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-unregistervm>.

- 기존 VM 등록 해제:

`VBoxManage unregistervm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_이름</span>

- 하드 디스크 이미지 파일, 모든 저장된 상태 파일, VM 로그 및 XML VM 머신 파일 삭제:

`VBoxManage unregistervm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_이름</span>` --delete`

- VM의 모든 파일 삭제:

`VBoxManage unregistervm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_이름</span>` --delete-all`
