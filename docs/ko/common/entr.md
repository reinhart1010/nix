---
layout: page
title: common/entr (한국어)
description: "파일이 변경되면 임의의 명령을 실행."
content_hash: 4905445de29446f2c7378ae9ad4682708f9ce94d
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/entr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/entr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/entr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# entr

파일이 변경되면 임의의 명령을 실행.
더 많은 정보: <https://eradman.com/entrproject/>.

- 하위 디렉터리의 파일이 변경되면 `make`로 다시 빌드:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ag -l</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- 현재 디렉터리에 `.c` 소스 파일이 변경되면 `make`로 다시 빌드하고 테스트:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.c</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'make && make test'</span>

- `ruby main.rb`를 실행하기 전에 이전에 생성된 ruby 하위 프로세스에 `SIGTERM`을 보냄:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.rb</span>` | entr -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby main.rb</span>

- 변경된 파일 (`/_`)을 인수로 사용하여 명령을 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.sql</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">psql -f</span>` /_`

- 화면을 지우고([c]lear) SQL 스크립트가 업데이트된 후 쿼리를 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo my.sql</span>` | entr -cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">psql -f</span>` /_`

- 소스 파일이 변경되면 프로젝트를 다시 빌드하고, 출력을 처음 몇 줄로 제한:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find src/</span>` | entr -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'make | sed 10q'</span>

- Node.js 서버를 시작하고 자동으로 로드(auto-[r]eload):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.js</span>` | entr -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node app.js</span>
