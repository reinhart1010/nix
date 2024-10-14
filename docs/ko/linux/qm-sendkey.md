---
layout: page
title: linux/qm-sendkey (한국어)
description: "QEMU 모니터 인코딩 키 이벤트를 가상 머신에 전송."
content_hash: bd35238ae3f4749bc1f4682497d1a1b89589bb47
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/qm-sendkey.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-sendkey.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm sendkey

QEMU 모니터 인코딩 키 이벤트를 가상 머신에 전송.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 특정 키 이벤트를 특정 가상 머신에 전송:

`qm sendkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- 루트 사용자가 키 이벤트를 전송하고 잠금을 무시하도록 허용:

`qm sendkey --skiplock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>
