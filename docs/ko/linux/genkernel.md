---
layout: page
title: linux/genkernel (한국어)
description: "Gentoo Linux에서 커널을 컴파일하고 설치하는 유틸리티."
content_hash: da40c0d11f5474b5fa125a9f94c66090bbbf88b8
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/genkernel.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/genkernel.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># genkernel

Gentoo Linux에서 커널을 컴파일하고 설치하는 유틸리티.
더 많은 정보: <https://wiki.gentoo.org/wiki/Genkernel>.

- 일반 커널을 자동으로 컴파일하고 설치:

`sudo genkernel all`

- bzImage|initramfs|kernel|ramdisk만 빌드하고 설치:

`sudo genkernel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bzImage|initramfs|kernel|ramdisk</span>

- 컴파일 및 설치 전에 커널 설정을 변경:

`sudo genkernel --menuconfig all`

- 사용자 지정 이름의 커널 생성:

`sudo genkernel --kernname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_지정_이름</span>` all`

- 기본 디렉토리 `/usr/src/linux` 외부의 커널 소스를 사용:

`sudo genkernel --kerneldir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` all`
