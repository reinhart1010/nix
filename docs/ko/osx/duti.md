---
layout: page
title: osx/duti (한국어)
description: "macOS에서 문서 유형 및 URL 스킴에 대한 기본 애플리케이션 설정."
content_hash: 8b887a5905e35a136f84cc61748093877ca76707
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/duti.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/duti.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/duti.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duti

macOS에서 문서 유형 및 URL 스킴에 대한 기본 애플리케이션 설정.
더 많은 정보: <https://github.com/moretension/duti>.

- HTML 문서의 기본 처리기로 Safari 설정:

`duti -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.Safari</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public.html</span>` all`

- `.m4v` 확장자를 가진 파일의 기본 뷰어로 VLC 설정:

`duti -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.videolan.vlc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">m4v</span>` viewer`

- ftp:// URL 스킴의 기본 처리기로 Finder 설정:

`duti -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.Finder</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp</span>`"`

- 주어진 확장자의 기본 애플리케이션 정보 표시:

`duti -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장자</span>

- 주어진 UTI의 기본 처리기 표시:

`duti -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uti</span>

- 주어진 UTI의 모든 처리기 표시:

`duti -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uti</span>
