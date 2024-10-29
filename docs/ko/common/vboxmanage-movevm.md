---
layout: page
title: common/vboxmanage-movevm (한국어)
description: "가상 머신(VM)을 호스트 시스템의 새로운 위치로 이동."
content_hash: 59ad6dd76cb67a7fe78d7740f22016399a451188
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/vboxmanage-movevm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vboxmanage-movevm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-movevm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage movevm

가상 머신(VM)을 호스트 시스템의 새로운 위치로 이동.
더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-movevm>.

- 지정한 가상 머신을 현재 위치로 이동:

`VBoxManage movevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>

- 가상 머신의 새 위치(전체 또는 상대 경로)를 지정:

`VBoxManage movevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>` --folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운_위치</span>
