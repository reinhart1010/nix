---
layout: page
title: common/whereis (한국어)
description: "명령의 바이너리, 소스 및 매뉴얼 페이지 파일을 찾습니다."
content_hash: 6b0a12f8ef676c63f17c35a9444f8060ae312d28
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/whereis.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/whereis.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/whereis.html
    icon: bi bi-globe
tldri18n_status: 2
---
# whereis

명령의 바이너리, 소스 및 매뉴얼 페이지 파일을 찾습니다.
더 많은 정보: <https://manned.org/whereis>.

- SSH에 대한 바이너리, 소스 및 매뉴얼 페이지 찾기:

`whereis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh</span>

- ls에 대한 바이너리 및 매뉴얼 페이지 찾기:

`whereis -bm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- gcc의 소스와 Git의 매뉴얼 페이지 찾기:

`whereis -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcc</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git</span>

- `/usr/bin/`에서만 gcc의 바이너리 찾기:

`whereis -b -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/bin/</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcc</span>

- 비정상적인 바이너리 찾기 (시스템에 하나 이상의 바이너리가 있는 경우):

`whereis -u *`

- 비정상적인 매뉴얼 항목을 가진 바이너리 찾기 (하나 이상의 매뉴얼이 설치된 경우):

`whereis -u -m *`
