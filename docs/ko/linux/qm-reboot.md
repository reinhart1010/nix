---
layout: page
title: linux/qm-reboot (한국어)
description: "가상 머신을 종료하고 보류 중인 변경 사항을 적용한 후 다시 시작."
content_hash: c9f8955aa3dfedeec948ae9f3b878af8a2398688
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/qm-reboot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-reboot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm reboot

가상 머신을 종료하고 보류 중인 변경 사항을 적용한 후 다시 시작.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 머신 재부팅:

`qm reboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 최대 10초 기다린 후 가상 머신 재부팅:

`qm reboot --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
