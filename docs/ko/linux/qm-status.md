---
layout: page
title: linux/qm-status (한국어)
description: "가상 머신 상태 표시."
content_hash: fff7eaf0149bd5ab583e0daf6028f62132f4d173
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/qm-status.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-status.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm status

가상 머신 상태 표시.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 특정 가상 머신의 상태 표시:

`qm status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 특정 가상 머신의 상세 상태 표시:

`qm status --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
