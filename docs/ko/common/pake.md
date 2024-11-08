---
layout: page
title: common/pake (한국어)
description: "Rust/Tauri를 사용하여 웹페이지를 데스크탑 앱으로 변환."
content_hash: 69a3a1147af2214d7bb47f13afd12aa94188bcf7
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pake

Rust/Tauri를 사용하여 웹페이지를 데스크탑 앱으로 변환.
더 많은 정보: <https://github.com/tw93/Pake>.

- 웹페이지 패키징:

`pake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/</span>

- 특정 창 크기로 웹페이지 패키징:

`pake --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800</span>` --height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">600</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/</span>

- 사용자 지정 애플리케이션 이름과 아이콘으로 웹페이지 패키징:

`pake --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Google</span>` --icon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/icon.ico</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/</span>

- 크기 조정이 불가능한 창으로 웹페이지 패키징:

`pake --no-resizable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/</span>

- 전체 화면 모드로 웹페이지 패키징:

`pake --fullscreen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/</span>

- 투명한 타이틀 바로 웹페이지 패키징:

`pake --transparent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/</span>
