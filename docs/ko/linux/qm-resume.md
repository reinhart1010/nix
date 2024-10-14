---
layout: page
title: linux/qm-resume (한국어)
description: "가상 머신 재개."
content_hash: aa3ba17df99d514d57e7d021a5d31c1e1723a1a6
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/qm-resume.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-resume.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm resume

가상 머신 재개.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 특정 가상 머신 재개:

`qm resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 잠금을 무시하고 특정 가상 머신 재개 (루트 권한 필요):

`sudo qm resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` --skiplock true`
