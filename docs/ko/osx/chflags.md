---
layout: page
title: osx/chflags (한국어)
description: "파일 또는 디렉토리 플래그 변경."
content_hash: 24aba26aeddb7b900d77446422ae5d704d8a3466
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/chflags.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/chflags.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/chflags.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chflags

파일 또는 디렉토리 플래그 변경.
더 많은 정보: <https://keith.github.io/xcode-man-pages/chflags.1.html>.

- 파일에 `hidden` 플래그 설정:

`chflags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hidden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에서 `hidden` 플래그 해제:

`chflags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nohidden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 디렉토리에 대해 `uchg` 플래그를 재귀적으로 설정:

`chflags -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uchg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 디렉토리에 대해 `uchg` 플래그를 재귀적으로 해제:

`chflags -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouchg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
