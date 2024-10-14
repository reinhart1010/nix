---
layout: page
title: linux/qm-wait (한국어)
description: "가상 머신이 중지될 때까지 대기."
content_hash: f766e37c79cb95fbc3d9898e4ddc542c17ff6630
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/qm-wait.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-wait.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm wait

가상 머신이 중지될 때까지 대기.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 머신이 중지될 때까지 대기:

`qm wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 가상 머신이 중지될 때까지 10초 동안 대기:

`qm wait --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>

- 종료 요청을 전송한 후 가상 머신이 중지될 때까지 10초 동안 대기:

`qm shutdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` && qm wait --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
