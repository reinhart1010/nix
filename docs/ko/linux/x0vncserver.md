---
layout: page
title: linux/x0vncserver (한국어)
description: "X 디스플레이용 TigerVNC 서버."
content_hash: 00a6e96eb1ed6dc639448feddee66795fad7c2f0
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/x0vncserver.html
    icon: bi bi-globe
tldri18n_status: 2
---
# x0vncserver

X 디스플레이용 TigerVNC 서버.
더 많은 정보: <https://tigervnc.org/doc/x0vncserver.html>.

- 암호 파일을 사용하여 VNC 서버 시작:

`x0vncserver -display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:0</span>` -passwordfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 포트를 사용하여 VNC 서버 시작:

`x0vncserver -display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:0</span>` -rfbport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>
