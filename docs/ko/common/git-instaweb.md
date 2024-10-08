---
layout: page
title: common/git-instaweb (한국어)
description: "GitWeb 서버를 실행하는 도우미 도구."
content_hash: 8a01916be9388151d4ad9119249975f8a91ee485
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-instaweb.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-instaweb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-instaweb.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-instaweb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git instaweb

GitWeb 서버를 실행하는 도우미 도구.
더 많은 정보: <https://git-scm.com/docs/git-instaweb>.

- 현재 Git 저장소에 대해 GitWeb 서버 실행:

`git instaweb --start`

- 로컬호스트에서만 리슨:

`git instaweb --start --local`

- 특정 포트에서 리슨:

`git instaweb --start --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- 지정된 HTTP 데몬 사용:

`git instaweb --start --httpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lighttpd|apache2|mongoose|plackup|webrick</span>

- 웹 브라우저도 자동으로 실행:

`git instaweb --start --browser`

- 현재 실행 중인 GitWeb 서버 중지:

`git instaweb --stop`

- 현재 실행 중인 GitWeb 서버 재시작:

`git instaweb --restart`
