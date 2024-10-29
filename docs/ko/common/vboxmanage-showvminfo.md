---
layout: page
title: common/vboxmanage-showvminfo (한국어)
description: "등록된 가상 머신에 대한 정보 표시."
content_hash: 8bf45042a8789c4448ac85676dbf101ac03e14c1
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/vboxmanage-showvminfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-showvminfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage-showvminfo

등록된 가상 머신에 대한 정보 표시.
더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-showvminfo>.

- 특정 가상 머신에 대한 정보 표시:

`VBoxManage showvminfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름|uuid</span>

- 특정 가상 머신에 대한 더 자세한 정보 표시:

`VBoxManage showvminfo --details `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름|uuid</span>

- 기계 판독 형식으로 정보 표시:

`VBoxManage showvminfo --machinereadable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름|uuid</span>

- 가상 머신이 암호화된 경우 암호 ID 지정:

`VBoxManage showvminfo --password-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름|uuid</span>

- 가상 머신이 암호화된 경우 암호 파일 지정:

`VBoxManage showvminfo --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패스워드_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름|uuid</span>

- 특정 가상 머신의 로그 표시:

`VBoxManage showvminfo --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름|uuid</span>
