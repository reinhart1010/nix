---
layout: page
title: common/chroot (한국어)
description: "특수 루트 디렉토리를 사용하여 명령 또는 대화형 쉘 실행."
content_hash: 9849b70dfe27f18c476ec5cee505c0308310917c
related_topics:
  - title: Deutsch version
    url: /de/common/chroot.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chroot.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chroot.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chroot.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/chroot.html
    icon: bi bi-globe
---
# chroot

특수 루트 디렉토리를 사용하여 명령 또는 대화형 쉘 실행.
더 많은 정보: <https://www.gnu.org/software/coreutils/chroot>.

- 새로운 루트 디렉토리로 명령어 실행:

`chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/새로운/루트/디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 사용할 사용자 및 그룹(ID 또는 이름) 지정:

`chroot --userspec=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자:그룹</span>
