---
layout: page
title: linux/debootstrap (한국어)
description: "기본 Debian 시스템 생성."
content_hash: e1d9ba1f6fe9b7dd10459f23531a7b81654bb8b9
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/debootstrap.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/debootstrap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/debootstrap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debootstrap

기본 Debian 시스템 생성.
더 많은 정보: <https://wiki.debian.org/Debootstrap>.

- `debian-root` 디렉터리 내에 Debian 안정 버전 시스템 생성:

`sudo debootstrap stable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/debian-root/</span>` http://deb.debian.org/debian`

- 필수 패키지만 포함하는 최소 시스템 생성:

`sudo debootstrap --variant=minbase stable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/debian-root/</span>

- 로컬 미러를 사용하여 `focal-root` 디렉터리 내에 Ubuntu 20.04 시스템 생성:

`sudo debootstrap focal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/focal-root/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file:///경로/대상/미러/</span>

- 부트스트랩된 시스템으로 전환:

`sudo chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/root</span>

- 사용 가능한 릴리스 나열:

`ls /usr/share/debootstrap/scripts/`
