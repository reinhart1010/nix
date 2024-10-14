---
layout: page
title: linux/qm-guest-exec-status (한국어)
description: "QEMU/KVM 가상 머신 관리자에서 게스트 에이전트에 의해 시작된 PID의 상태를 출력."
content_hash: cd12b307a1fd83a10fe1a66af661da121ba571ba
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/qm-guest-exec-status.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-guest-exec-status.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm guest exec-status

QEMU/KVM 가상 머신 관리자에서 게스트 에이전트에 의해 시작된 PID의 상태를 출력.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 특정 PID의 상태 출력:

`qm guest exec-status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
