---
layout: page
title: linux/qm-guest-passwd (한국어)
description: "QEMU/KVM 가상 머신 관리자에서 사용자의 비밀번호 설정."
content_hash: f0157c9ed0a60fabf829f1745b75e8418a407e7f
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/qm-guest-passwd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-guest-passwd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm guest passwd

QEMU/KVM 가상 머신 관리자에서 사용자의 비밀번호 설정.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 가상 머신 내 특정 사용자에 대해 비밀번호를 대화식으로 설정:

`qm guest passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>

- 이미 해시된 비밀번호를 가상 머신 내 특정 사용자에 대해 대화식으로 설정:

`qm guest passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --crypted 1`
