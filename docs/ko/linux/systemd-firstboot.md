---
layout: page
title: linux/systemd-firstboot (한국어)
description: "시스템의 첫 부팅 시 또는 부팅 전에 기본 시스템 설정 초기화."
content_hash: 00f596844f5fa37492f596adbeac6c17eed30f6c
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/systemd-firstboot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-firstboot

시스템의 첫 부팅 시 또는 부팅 전에 기본 시스템 설정 초기화.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-firstboot.html>.

- 호스트 시스템의 루트 디렉토리 대신 지정된 디렉토리에서 작동:

`sudo systemd-firstboot --root=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/루트_디렉토리</span>

- 시스템 키보드 레이아웃 설정:

`sudo systemd-firstboot --keymap=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키맵</span>

- 시스템 호스트명 설정:

`sudo systemd-firstboot --hostname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>

- 루트 사용자의 비밀번호 설정:

`sudo systemd-firstboot --root-password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 특정 기본 설정을 사용자에게 인터랙티브하게 요청:

`sudo systemd-firstboot --prompt=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정</span>

- 관련 파일이 이미 존재해도 강제로 설정 작성:

`sudo systemd-firstboot --force`

- `systemd-firstboot`에 의해 설정된 기존 파일 모두 제거:

`sudo systemd-firstboot --reset`

- 시스템의 루트 사용자의 비밀번호 제거:

`sudo systemd-firstboot --delete-root-password`
