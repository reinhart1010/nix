---
layout: page
title: common/vboxmanage-startvm (한국어)
description: "가상 머신 시작."
content_hash: e2c639ee02110d41c968c787bbd76494d83c5194
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/vboxmanage-startvm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-startvm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage-startvm

가상 머신 시작.
더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-startvm>.

- 가상 머신 시작:

`VBoxManage startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름|uuid</span>

- 지정된 UI 모드로 가상 머신 시작:

`VBoxManage startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름|uuid</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">headless|gui|sdl|separate</span>

- 암호화된 가상 머신을 시작하기 위해 암호 파일 지정:

`VBoxManage startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름|uuid</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호_파일</span>

- 암호화된 가상 머신을 시작하기 위해 암호 ID 지정:

`VBoxManage startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름|uuid</span>` --password-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호_id</span>

- 환경 변수 쌍 이름 값을 사용하여 가상 머신 시작:

`VBoxManage startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름|uuid</span>` --put-env=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>
