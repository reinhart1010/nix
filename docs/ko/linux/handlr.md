---
layout: page
title: linux/handlr (한국어)
description: "기본 애플리케이션을 관리합니다."
content_hash: a4ef2f9c7447ef6348c22be1a7ee76613f712c77
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/handlr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# handlr

기본 애플리케이션을 관리합니다.
더 많은 정보: <https://github.com/chmln/handlr>.

- 기본 애플리케이션에서 URL 열기:

`handlr open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 기본 PDF 뷰어에서 PDF 열기:

`handlr open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- PNG 파일의 기본 애플리케이션으로 `imv` 설정:

`handlr set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imv.desktop</span>

- 모든 오디오 파일의 기본 애플리케이션으로 MPV 설정:

`handlr set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'audio/*'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv.desktop</span>

- 모든 기본 앱 나열:

`handlr list`

- PNG 파일의 기본 애플리케이션 출력:

`handlr get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.png</span>
