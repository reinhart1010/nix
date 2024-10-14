---
layout: page
title: linux/qm-delsnapshot (한국어)
description: "가상 머신 스냅샷 삭제."
content_hash: 87307d159963cbe95dd47abed5fd2a8e66d39e67
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/qm-delsnapshot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-delsnapshot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm delsnapshot

가상 머신 스냅샷 삭제.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 스냅샷 삭제:

`qm delsnapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_이름</span>

- 구성 파일에서 스냅샷 삭제 (디스크 스냅샷 제거가 실패하더라도 강제 삭제):

`qm delsnapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_이름</span>` --force 1`
