---
layout: page
title: linux/qm-cloudinit-dump (한국어)
description: "cloudinit 구성 파일 생성."
content_hash: acbf08c9a302ddb573a0fbf2f87daa338892c08b
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/qm-cloudinit-dump.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-cloudinit-dump.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm cloudinit dump

cloudinit 구성 파일 생성.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 특정 구성 유형에 대한 cloudinit 파일 생성:

`qm cloudinit dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">meta|network|user</span>
