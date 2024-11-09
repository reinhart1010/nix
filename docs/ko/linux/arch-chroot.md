---
layout: page
title: linux/arch-chroot (한국어)
description: "Arch Linux 설치 과정에서 도움이 되는 향상된 `chroot` 명령어."
content_hash: e3a103a9de3ef4a1fda734eb5df61550770d9d84
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/linux/arch-chroot.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/arch-chroot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arch-chroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arch-chroot

Arch Linux 설치 과정에서 도움이 되는 향상된 `chroot` 명령어.
더 많은 정보: <https://manned.org/arch-chroot.8>.

- 새 루트 디렉토리에서 인터랙티브 셸(기본적으로 Bash)을 시작:

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운/루트</span>

- 현재 사용자 외에 다른 사용자로 셸 실행:

`arch-chroot -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운/루트</span>

- 새 루트 디렉토리에서 기본 Bash 대신 사용자 지정 명령 실행:

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운/루트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자들</span>

- 기본 Bash 대신 다른 셸 지정(이 경우, 대상 시스템에 `zsh` 패키지가 설치되어 있어야 함):

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운/루트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>
