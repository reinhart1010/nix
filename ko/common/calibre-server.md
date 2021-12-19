---
layout: page
title: common/calibre-server (한국어)
description: "네트워크를 통해 전자책을 배포하는 데 사용할 수 있는 서버 어플리케이션."
content_hash: b2026f00c41e636c8820b3a1dc5cd526d3e36169
related_topics:
  - title: English version
    url: /en/common/calibre-server.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/calibre-server.html
    icon: bi bi-globe
---
# calibre-server

네트워크를 통해 전자책을 배포하는 데 사용할 수 있는 서버 어플리케이션.
이전에 GUI 또는 보정기능을 사용하여 전자책을 라이브러리로 가져와야 함.
Calibre 전자책 라이브러리의 일부.
더 많은 정보: <https://manual.calibre-ebook.com/generated/en/calibre-server.html>.

- 전자책을 배포할 서버 시작. http://localhost:8080에 연결:

`calibre-server`

- 다른 포트에서 서버 시작. http://localhost:port에 연결:

`calibre-server --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트번호</span>

- 서버를 암호로 보호:

`calibre-server --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>
