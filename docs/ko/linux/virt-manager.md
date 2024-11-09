---
layout: page
title: linux/virt-manager (한국어)
description: "KVM 및 Xen 가상 머신과 LXC 컨테이너를 관리하기 위한 데스크톱 사용자 인터페이스."
content_hash: 24f6a1ad3b36244cb306bcf00f0fa8a26fff7337
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/virt-manager.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/virt-manager.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># virt-manager

KVM 및 Xen 가상 머신과 LXC 컨테이너를 관리하기 위한 데스크톱 사용자 인터페이스.
더 많은 정보: <https://manned.org/virt-manager.1>.

- GUI 실행:

`virt-manager`

- 하이퍼바이저에 연결:

`virt-manager --connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하이퍼바이저_URI</span>

- 시작 시 virt-manager 프로세스를 백그라운드로 포크하지 않음:

`virt-manager --no-fork`

- 디버그 출력 표시:

`virt-manager --debug`

- "새로운 VM" 마법사 열기:

`virt-manager --show-domain-creator`

- 특정 가상 머신/컨테이너에 대한 도메인 세부 정보 창 표시:

`virt-manager --show-domain-editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|ID|UUID</span>

- 특정 가상 머신/컨테이너에 대한 도메인 성능 창 표시:

`virt-manager --show-domain-performance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|ID|UUID</span>

- 연결 세부 정보 창 표시:

`virt-manager --show-host-summary`
