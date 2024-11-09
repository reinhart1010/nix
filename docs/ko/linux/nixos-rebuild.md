---
layout: page
title: linux/nixos-rebuild (한국어)
description: "NixOS 머신을 재구성합니다."
content_hash: 69ef1db42f0906811f466bf7ec493310b113e943
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/linux/nixos-rebuild.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/nixos-rebuild.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nixos-rebuild.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nixos-rebuild

NixOS 머신을 재구성합니다.
더 많은 정보: <https://nixos.org/nixos/manual/#sec-changing-config>.

- 새로운 설정을 빌드하고 전환하며, 부팅 기본값으로 설정:

`sudo nixos-rebuild switch`

- 새로운 설정을 빌드하고 전환하며, 부팅 기본값으로 설정하고 부팅 항목 이름 지정:

`sudo nixos-rebuild switch -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 새로운 설정을 빌드하고 전환하며, 부팅 기본값으로 설정하고 업데이트 설치:

`sudo nixos-rebuild switch --upgrade`

- 설정 변경 사항을 롤백하고 이전 세대로 전환:

`sudo nixos-rebuild switch --rollback`

- 새로운 설정을 빌드하여 부팅 기본값으로 설정하지만, 전환하지 않음:

`sudo nixos-rebuild boot`

- 새로운 설정을 빌드하고 활성화하지만, 부팅 항목을 만들지 않음 (테스트 용도):

`sudo nixos-rebuild test`

- 설정을 빌드하고 가상 머신에서 열기:

`sudo nixos-rebuild build-vm`
