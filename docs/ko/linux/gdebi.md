---
layout: page
title: linux/gdebi (한국어)
description: "`.deb` 파일을 쉽게 설치합니다."
content_hash: 6843b7e88f3deb8a0da15fc4e7aa22657880158a
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/gdebi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gdebi

`.deb` 파일을 쉽게 설치합니다.
더 많은 정보: <https://www.commandlinux.com/man-page/man1/gdebi.1.html>.

- 로컬 `.deb` 패키지를 설치하고 의존성을 해결하여 설치:

`gdebi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.deb</span>

- 진행 정보를 표시하지 않음:

`gdebi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.deb</span>` --quiet`

- APT 구성 옵션 설정:

`gdebi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.deb</span>` --option=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">APT_옵션</span>

- 대체 루트 디렉토리 사용:

`gdebi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.deb</span>` --root=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/루트_폴더</span>

- 버전 표시:

`gdebi --version`
