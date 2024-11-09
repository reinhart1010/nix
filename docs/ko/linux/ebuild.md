---
layout: page
title: linux/ebuild (한국어)
description: "Gentoo Portage 시스템에 대한 저수준 인터페이스."
content_hash: 76e03286f0ab6f5247fad90241bf1801088a78ef
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ebuild.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ebuild

Gentoo Portage 시스템에 대한 저수준 인터페이스.
더 많은 정보: <https://wiki.gentoo.org/wiki/Ebuild>.

- 패키지 매니페스트 생성 또는 업데이트:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ebuild</span>` manifest`

- 빌드 파일의 임시 빌드 디렉터리 정리:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ebuild</span>` clean`

- 소스가 존재하지 않을 경우 소스 가져오기:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ebuild</span>` fetch`

- 소스를 임시 빌드 디렉터리에 추출:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ebuild</span>` unpack`

- 추출된 소스 컴파일:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ebuild</span>` compile`

- 임시 설치 디렉터리에 패키지 설치:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ebuild</span>` install`

- 라이브 파일 시스템에 임시 파일 설치:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ebuild</span>` qmerge`

- 지정된 ebuild 파일의 소스 가져오기, 추출, 컴파일, 설치 및 qmerge 수행:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ebuild</span>` merge`
