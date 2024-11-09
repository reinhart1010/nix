---
layout: page
title: linux/mkinitcpio (한국어)
description: "지정된 프리셋을 기반으로 Linux 커널 부팅을 위한 초기 램디스크 환경을 생성합니다."
content_hash: 7e9dc00042b75513559254fe259187bf5d3d5d4c
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mkinitcpio.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkinitcpio.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkinitcpio

지정된 프리셋을 기반으로 Linux 커널 부팅을 위한 초기 램디스크 환경을 생성합니다.
더 많은 정보: <https://manned.org/mkinitcpio.8>.

- 실행하지 않고 수행할 작업을 출력하는 드라이 런 수행:

`mkinitcpio`

- `linux` 프리셋을 기반으로 램디스크 환경 생성:

`mkinitcpio --preset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux</span>

- `linux-lts` 프리셋을 기반으로 램디스크 환경 생성:

`mkinitcpio --preset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux-lts</span>

- 모든 기존 프리셋을 기반으로 램디스크 환경 생성 (`/etc/mkinitcpio.conf`의 변경 후 모든 initramfs 이미지를 다시 생성하는 데 사용):

`mkinitcpio --allpresets`

- 대체 설정 파일을 사용하여 initramfs 이미지 생성:

`mkinitcpio --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/mkinitcpio.conf</span>` --generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/initramfs.img</span>

- 현재 실행 중인 커널이 아닌 다른 커널에 대한 initramfs 이미지 생성 (설치된 커널 릴리스는 `/usr/lib/modules/`에 있음):

`mkinitcpio --kernel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커널_버전</span>` --generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/initramfs.img</span>

- 사용 가능한 모든 훅 나열:

`mkinitcpio --listhooks`

- 특정 훅에 대한 도움말 표시:

`mkinitcpio --hookhelp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">훅_이름</span>
