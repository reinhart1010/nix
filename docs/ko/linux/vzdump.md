---
layout: page
title: linux/vzdump (한국어)
description: "가상 머신 및 컨테이너 백업 유틸리티."
content_hash: 3c425fcb655423d3882df63d321a289cad9311c5
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/vzdump.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/vzdump.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vzdump

가상 머신 및 컨테이너 백업 유틸리티.
더 많은 정보: <https://pve.proxmox.com/pve-docs/vzdump.1.html>.

- 스냅샷을 제외하고 기본 덤프 디렉토리(보통 `/var/lib/vz/dump/`)에 게스트 가상 머신을 덤프:

`vzdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- ID가 101, 102, 103인 게스트 가상 머신 백업:

`vzdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">101 102 103</span>

- 특정 모드를 사용하여 게스트 가상 머신 덤프:

`vzdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suspend|snapshot</span>

- 모든 게스트 시스템을 백업하고 루트 및 관리자 사용자에게 알림 이메일 전송:

`vzdump --all --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suspend</span>` --mailto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root</span>` --mailto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">admin</span>

- 스냅샷 모드 사용(다운타임 필요 없음) 및 기본이 아닌 덤프 디렉토리 사용:

`vzdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` --dumpdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot</span>

- ID가 101 및 102인 것 제외한 모든 게스트 가상 머신 백업:

`vzdump --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suspend</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">101, 102</span>
