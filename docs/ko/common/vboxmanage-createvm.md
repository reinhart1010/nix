---
layout: page
title: common/vboxmanage-createvm (한국어)
description: "새 가상 머신 생성."
content_hash: df5b3d993ac868e1b0f0ecbcdaa30c6cabe3119f
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/vboxmanage-createvm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-createvm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage-createvm

새 가상 머신 생성.
더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-createvm>.

- 기본 설정으로 새 VM 생성:

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>

- VM 구성 파일이 저장될 기본 폴더 설정:

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>` --basefolder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 가져온 VM의 게스트 OS 유형 설정 (`VBoxManage list ostypes` 중 하나):

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>` --ostype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os유형</span>

- 생성된 VM을 VirtualBox에 등록:

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>` --register`

- VM을 지정된 그룹에 설정:

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>` --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹1,그룹2,...</span>

- VM의 전역 고유 식별자(UUID) 설정:

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>` --uuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>

- 암호화에 사용할 암호화 방식 설정:

`VBoxManage createvm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>` --cipher `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AES-128|AES-256</span>
