---
layout: page
title: linux/qm-rescan (한국어)
description: "모든 스토리지를 다시 스캔하고 가상 머신의 디스크 크기와 사용되지 않는 디스크 이미지를 업데이트."
content_hash: c1470615cd1b313b0c25ebbabb582a200cdcf7e9
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/qm-rescan.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-rescan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm rescan

모든 스토리지를 다시 스캔하고 가상 머신의 디스크 크기와 사용되지 않는 디스크 이미지를 업데이트.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 특정 가상 머신의 모든 스토리지를 다시 스캔하고 디스크 크기와 사용되지 않는 디스크 이미지를 업데이트:

`qm rescan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 특정 가상 머신에 대해 다시 스캔을 시뮬레이션하고 구성에 아무런 변경도 기록하지 않음:

`qm rescan --dryrun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
