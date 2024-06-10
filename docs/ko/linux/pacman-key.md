---
layout: page
title: linux/pacman-key (한국어)
description: "GnuPG를 사용하여 pacman의 키링을 관리하는 래퍼 스크립트."
content_hash: ae1cf7391819be7ef46df891b803b114ef6a3797
last_modified_at: 2024-06-10
related_topics:
  - title: English version
    url: /en/linux/pacman-key.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-key.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-key.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman-key

GnuPG를 사용하여 pacman의 키링을 관리하는 래퍼 스크립트.
같이 보기: `pacman`.
더 많은 정보: <https://man.archlinux.org/man/pacman-key>.

- `pacman` 키링 초기화:

`sudo pacman-key --init`

- 기본 Arch Linux 키 추가:

`sudo pacman-key --populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archlinux</span>

- 공개 키링에서 키 나열:

`pacman-key --list-keys`

- 지정된 키 추가:

`sudo pacman-key --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키파일.gpg</span>

- 키 서버에서 키 수신:

`sudo pacman-key --recv-keys "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|name|email</span>`"`

- 특정 키의 지문 출력:

`pacman-key --finger "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|name|email</span>`"`

- 가져온 키를 로컬에서 서명:

`sudo pacman-key --lsign-key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|name|email</span>`"`

- 특정 키 제거:

`sudo pacman-key --delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|name|email</span>`"`
