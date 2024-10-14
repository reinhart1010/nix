---
layout: page
title: linux/qm-cloud-init (한국어)
description: "Proxmox Virtual Environment (PVE)에서 관리하는 가상 머신에 대한 cloudinit 설정 구성."
content_hash: 0387b391cd8a49782e370b2b12ea6dc3445af686
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/qm-cloud-init.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-cloud-init.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm cloud init

Proxmox Virtual Environment (PVE)에서 관리하는 가상 머신에 대한 cloudinit 설정 구성.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 특정 사용자에 대한 cloudinit 설정 구성 및 사용자 비밀번호 설정:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` -user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` -password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 특정 사용자에 대한 cloudinit 설정 구성 및 특정 SSH 키로 사용자 비밀번호 설정:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` -user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` -password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -sshkey=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh_키</span>

- 특정 가상 머신의 호스트네임 설정:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` -hostname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트네임</span>

- 특정 가상 머신의 네트워크 인터페이스 설정 구성:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` -ipconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ipconfig</span>

- 가상 머신에서 `cloud-init`이 실행되기 전에 수행할 셸 스크립트 구성:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` -pre `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트</span>
