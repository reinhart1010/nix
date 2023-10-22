---
layout: page
title: common/virsh (한국어)
description: "virsh 게스트 도메인을 관리합니다. (NOTE: 'guest_id'는 게스트의 아이디, 이름 또는 UUID일 수 있습니다)."
content_hash: b5d75c530d3fa0718cecd21df20159efe90a1b1c
last_modified_at: 2023-10-22
related_topics:
  - title: English version
    url: /en/common/virsh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh.html
    icon: bi bi-globe
---
# virsh

virsh 게스트 도메인을 관리합니다. (NOTE: 'guest_id'는 게스트의 아이디, 이름 또는 UUID일 수 있습니다).
`virsh list`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://libvirt.org/virshcmdref.html>.

- 하이퍼아비저 세션에 연결:

`virsh connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qemu:///system</span>

- 모든 도메인 나열:

`virsh list --all`

- 게스트 구성 파일 덤프:

`virsh dumpxml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게스트 아이디</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/게스트 구성 파일.xml</span>

- 구성 파일에서 게스트 만들기:

`virsh create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성 파일.xml</span>

- 게스트의 구성 파일 편집 (편집기는 $EDITOR로 변경할 수 있음):

`virsh edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게스트_아이디</span>

- 게스트 시작/재부팅/종료/일시 중지/재개:

`virsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게스트_아이디</span>

- 게스트의 현재 상태를 파일에 저장:

`virsh save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게스트_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름</span>

- 실행 중인 게스트 삭제:

`virsh destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게스트_아이디</span>` && virsh undefine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게스트_아이디</span>
