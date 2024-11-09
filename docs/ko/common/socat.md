---
layout: page
title: common/socat (한국어)
description: "다목적 릴레이(SOcket CAT)."
content_hash: 4deafd27a05e8661c656f5b395d8507b4dc0a1a2
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/socat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/socat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># socat

다목적 릴레이(SOcket CAT).
더 많은 정보: <http://www.dest-unreach.org/socat/>.

- 포트를 수신 대기하고 연결을 기다리며 데이터를 표준 입력/출력으로 전송:

`sudo socat - TCP-LISTEN:8080,fork`

- SSL을 사용하여 포트를 수신 대기하고 표준 출력으로 출력:

`sudo socat OPENSSL-LISTEN:4433,reuseaddr,cert=./cert.pem,cafile=./ca.cert.pem,key=./key.pem,verify=0 STDOUT`

- 호스트와 포트에 연결을 생성하고 표준 입력/출력의 데이터를 연결된 호스트로 전송:

`sudo socat - TCP4:www.example.com:80`

- 로컬 포트의 수신 데이터를 다른 호스트와 포트로 전달:

`sudo socat TCP-LISTEN:80,fork TCP4:www.example.com:80`
