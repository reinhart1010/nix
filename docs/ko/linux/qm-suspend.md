---
layout: page
title: linux/qm-suspend (한국어)
description: "Proxmox Virtual Environment (PVE)에서 가상 머신(VM)을 일시 중단합니다."
content_hash: fc1b5610d304e3775a6dc6fe0d9928756e0c9c50
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/qm-suspend.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-suspend.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm suspend

Proxmox Virtual Environment (PVE)에서 가상 머신(VM)을 일시 중단합니다.
`--skiplock` 및 `--skiplockstorage` 플래그는 데이터 손상을 초래할 수 있으므로 주의해서 사용해야 합니다.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- ID로 가상 머신 일시 중단:

`qm suspend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정수</span>

- VM을 일시 중단할 때 잠금 확인 건너뛰기:

`qm suspend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정수</span>` --skiplock`

- VM을 일시 중단할 때 스토리지 잠금 확인 건너뛰기:

`qm suspend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정수</span>` --skiplockstorage`
