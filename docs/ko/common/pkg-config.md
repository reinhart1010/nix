---
layout: page
title: common/pkg-config (한국어)
description: "애플리케이션 컴파일을 위한 설치된 라이브러리의 세부 정보를 제공."
content_hash: 9463e1aab6febc0a0a52b381ba0d36ad1531376a
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pkg-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg-config

애플리케이션 컴파일을 위한 설치된 라이브러리의 세부 정보를 제공.
더 많은 정보: <https://www.freedesktop.org/wiki/Software/pkg-config/>.

- 라이브러리 및 그 의존성 목록 확인:

`pkg-config --libs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라이브러리1 라이브러리2 ...</span>

- 라이브러리, 그 의존성 및 gcc에 대한 적절한 cflags 목록 확인:

`pkg-config --cflags --libs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라이브러리1 라이브러리2 ...</span>

- libgtk-3, libwebkit2gtk-4.0 및 모든 의존성을 사용하여 코드 컴파일:

`c++ example.cpp $(pkg-config --cflags --libs gtk+-3.0 webkit2gtk-4.0) -o example`
