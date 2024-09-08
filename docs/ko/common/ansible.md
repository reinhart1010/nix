---
layout: page
title: common/ansible (한국어)
description: "SSH를 통해 컴퓨터 그룹을 원격으로 관리. (`/etc/ansible/hosts` 파일을 사용하여 새 그룹/호스트를 추가하십시오)."
content_hash: 9355c4f483a51bafa48a9019a1f0d471ffb40db9
last_modified_at: 2024-09-08
related_topics:
  - title: Deutsch version
    url: /de/common/ansible.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ansible.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ansible.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ansible.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible

SSH를 통해 컴퓨터 그룹을 원격으로 관리. (`/etc/ansible/hosts` 파일을 사용하여 새 그룹/호스트를 추가하십시오).
`ansible galaxy`와 같은 일부 하위 명령에는 자체 사용 설명서가 있음.
더 많은 정보: <https://www.ansible.com/>.

- 그룹에 속한 호스트 목록:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹명</span>` --list-hosts`

- 핑 모듈을 호출하여 호스트 그룹 핑:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹명</span>` -m ping`

- 설정 모듈을 호출하여 호스트 그룹에 대한 사실 표시:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹명</span>` -m setup`

- 명령 모듈을 인수로 호출하여 호스트 그룹에서 명령어 실행:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹명</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">나의_명령어</span>`'`

- 관리자 권한으로 명령어 실행:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹명</span>` --become --ask-become-pass -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">나의_명령어</span>`'`

- 사용자 정의 인벤토리 파일을 사용하여 명령어 실행:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인벤토리_파일</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">나의_명령어</span>`'`

- 인벤토리의 그룹을 나열:

`ansible localhost -m debug -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var=groups.keys()</span>`'`
