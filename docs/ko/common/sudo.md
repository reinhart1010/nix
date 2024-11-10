---
layout: page
title: common/sudo (한국어)
description: "단일 명령을 슈퍼유저 또는 다른 사용자로 실행."
content_hash: dc5bb38d832949fcdbb6d1446fbff8065ba69aa8
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/sudo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/sudo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/sudo.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/sudo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/sudo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sudo

단일 명령을 슈퍼유저 또는 다른 사용자로 실행.
더 많은 정보: <https://www.sudo.ws/sudo.html>.

- 명령을 슈퍼유저로 실행:

`sudo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">less /var/log/syslog</span>

- 기본 편집기로 파일을 슈퍼유저 권한으로 편집:

`sudo --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/fstab</span>

- 다른 사용자 및/또는 그룹으로 명령 실행:

`sudo --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` --group=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id -a</span>

- 마지막 명령을 `sudo`로 접두사 붙여서 반복 (Bash, Zsh 등에서만 가능):

`sudo !!`

- 슈퍼유저 권한으로 기본 셸 시작하고 로그인 관련 파일(`.profile`, `.bash_profile` 등) 실행:

`sudo --login`

- 환경을 변경하지 않고 슈퍼유저 권한으로 기본 셸 시작:

`sudo --shell`

- 지정된 사용자로 기본 셸 시작, 사용자의 환경을 로드하고 로그인 관련 파일(`.profile`, `.bash_profile` 등) 읽기:

`sudo --login --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>

- 호출한 사용자에 대해 허용된 (및 금지된) 명령 목록 표시:

`sudo --list`
