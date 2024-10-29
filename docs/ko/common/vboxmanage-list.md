---
layout: page
title: common/vboxmanage-list (한국어)
description: "Oracle VM VirtualBox 소프트웨어 및 관련 서비스에 대한 정보를 나열합니다."
content_hash: a51c353549cbe03f11820d3d31b88bf604ed94bd
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/vboxmanage-list.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-list.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage-list

Oracle VM VirtualBox 소프트웨어 및 관련 서비스에 대한 정보를 나열합니다.
더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-list>.

- 모든 VirtualBox 가상 머신 나열:

`VBoxManage list vms`

- 호스트 시스템에서 사용 가능한 DHCP 서버 표시:

`VBoxManage list dhcpservers`

- 현재 설치된 Oracle VM VirtualBox 확장팩 표시:

`VBoxManage list extpacks`

- 모든 가상 머신 그룹 표시:

`VBoxManage list groups`

- VirtualBox에서 현재 사용 중인 가상 디스크 설정 표시:

`VBoxManage list hdds`

- 호스트 시스템에서 사용 가능한 호스트 전용 네트워크 인터페이스 표시:

`VBoxManage list hostonlyifs`

- 현재 실행 중인 가상 머신 목록 표시:

`VBoxManage list runningvms`

- 호스트 시스템 정보 표시:

`VBoxManage list hostinfo`
