---
layout: page
title: osx/pkgutil (한국어)
description: "Mac OS X 설치 패키지 및 영수증을 조회하고 조작."
content_hash: 918459e9293f5e9eda248d2fa34cbd86d7c852d1
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/pkgutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkgutil

Mac OS X 설치 패키지 및 영수증을 조회하고 조작.
더 많은 정보: <https://keith.github.io/xcode-man-pages/pkgutil.1.html>.

- 모든 설치된 패키지의 패키지 ID 나열:

`pkgutil --pkgs`

- 패키지 파일의 암호화 서명 검증:

`pkgutil --check-signature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.pkg</span>

- 주어진 ID의 설치된 패키지의 모든 파일 나열:

`pkgutil --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.microsoft.Word</span>

- 패키지 파일의 내용을 디렉토리에 추출:

`pkgutil --expand-full `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.pkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
