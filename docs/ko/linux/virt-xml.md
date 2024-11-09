---
layout: page
title: linux/virt-xml (한국어)
description: "명령줄 옵션을 사용하여 libvirt 도메인 XML 파일을 편집합니다."
content_hash: 0513f9501934f8df2bb04b3f835500aeb91c797b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/virt-xml.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/virt-xml.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># virt-xml

명령줄 옵션을 사용하여 libvirt 도메인 XML 파일을 편집합니다.
참고: '도메인'은 기존 VM의 이름, UUID 또는 ID를 의미합니다 (참조: tldr virsh).
더 많은 정보: <https://github.com/virt-manager/virt-manager/blob/main/man/virt-xml.rst>.

- 특정 옵션에 대한 모든 하위 옵션 나열:

`virt-xml --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>`=?`

- 디스크, 네트워크 및 부트에 대한 모든 하위 옵션 나열:

`virt-xml --disk=? --network=? --boot=?`

- 특정 도메인의 값을 편집:

`virt-xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>` --edit --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위옵션</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_값</span>

- 특정 도메인의 설명 변경:

`virt-xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>` --edit --metadata description="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_설명</span>`"`

- 특정 도메인에 대한 부팅 장치 메뉴 활성화/비활성화:

`virt-xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>` --edit --boot bootmenu=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- 실행 중인 VM에 호스트 USB 허브 연결 (참조: tldr lsusb):

`virt-xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>` --update --add-device --hostdev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버스</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>
