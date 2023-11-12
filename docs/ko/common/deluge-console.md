---
layout: page
title: common/deluge-console (한국어)
description: "Deluge BitTorrent 클라이언트를 위한 대화형 인터페이스."
content_hash: a3401c51db8aa895e7fd39e6ba61d2d85626761f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/deluge-console.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/deluge-console.html
    icon: bi bi-globe
tldri18n_status: 2
---
# deluge-console

Deluge BitTorrent 클라이언트를 위한 대화형 인터페이스.
더 많은 정보: <https://deluge-torrent.org>.

- 대화형 콘솔 인터페이스 시작:

`deluge-console`

- Deluge 데몬 객체에 연결:

`connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트번호</span>

- 데몬에 토렌트 추가:

`add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|파일/경로</span>

- 모든 토렌트에 대한 정보 표시:

`info`

- 특정 토렌트에 대한 정보 표시:

`info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트_아이디</span>

- 토렌트 일시정지:

`pause `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트_아이디</span>

- 토렌트 재시작:

`resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트_아이디</span>

- 데몬으로부터 토렌트 제거:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트_아이디</span>
