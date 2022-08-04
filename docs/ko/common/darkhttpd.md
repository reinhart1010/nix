---
layout: page
title: common/darkhttpd (한국어)
description: "Darkhttpd 웹 서버."
content_hash: a0001d164a17ee4701369fb29a0fd7749dd3b18e
related_topics:
  - title: English version
    url: /en/common/darkhttpd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/darkhttpd.html
    icon: bi bi-globe
---
# darkhttpd

Darkhttpd 웹 서버.
더 많은 정보: <https://unix4lyfe.org/darkhttpd>.

- 지정된 문서 경로를 제공하는 서버 시작:

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/문서</span>

- 지정된 포트에서 서버 시작(루트가 아닌 사용자로 시작되는 경우 8080포트가 기본값):

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/문서</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트번호</span>

- 지정된 IP 주소에서만 수신 (기본적으로 서버는 모든 인터페이스에서 수신):

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/문서</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip주소</span>
