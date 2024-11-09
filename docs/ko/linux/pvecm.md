---
layout: page
title: linux/pvecm (한국어)
description: "Proxmox VE 클러스터 관리자."
content_hash: 9a04739f3cd0fb341f9f297d13825bc702ae0543
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pvecm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pvecm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pvecm

Proxmox VE 클러스터 관리자.
더 많은 정보: <https://pve.proxmox.com/pve-docs/pvecm.1.html>.

- 현재 노드를 기존 클러스터에 추가:

`pvecm add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명_또는_IP</span>

- 클러스터 구성에 노드 추가 (내부 사용):

`pvecm addnode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드</span>

- 이 노드에서 사용 가능한 클러스터 가입 API 버전 표시:

`pvecm apiver`

- 새 클러스터 구성 생성:

`pvecm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터명</span>

- 클러스터 구성에서 노드 제거:

`pvecm delnode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드</span>

- 클러스터 노드에 대한 로컬 보기 표시:

`pvecm nodes`

- 클러스터 상태에 대한 로컬 보기 표시:

`pvecm status`
