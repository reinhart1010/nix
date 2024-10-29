---
layout: page
title: common/vboxmanage-controlvm (한국어)
description: "현재 실행 중인 가상 머신의 상태 및 설정 변경."
content_hash: 554833ff2378c6ddaf316ad37e73961b7c0df6af
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/vboxmanage-controlvm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-controlvm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage-controlvm

현재 실행 중인 가상 머신의 상태 및 설정 변경.
더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-controlvm>.

- 가상 머신의 실행을 일시 중지:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_이름</span>` pause`

- 일시 중지된 가상 머신의 실행 재개:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_이름</span>` resume`

- 가상 머신에 콜드 리셋 수행:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_이름</span>` reset`

- 가상 머신의 전원을 컴퓨터의 전원 케이블을 뽑는 것과 동일한 효과로 끄기:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_이름</span>` poweroff`

- 가상 머신을 종료하고 현재 상태 저장:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_이름</span>` savestate`

- 가상 머신에 ACPI(Advanced Configuration and Power Interface) 종료 신호 보내기:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_이름</span>` acpipowerbutton`

- 게스트 OS에 가상 머신의 자체 재부팅 명령 보내기:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_이름</span>` reboot`

- 상태를 저장하지 않고 가상 머신 종료:

`VBoxManage controlvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid|vm_이름</span>` shutdown`
