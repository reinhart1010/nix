---
layout: page
title: common/ruby (한국어)
description: "Ruby 프로그래밍 언어 인터프리터."
content_hash: 6b1e6642b7e2b7e6576b5469aea755b03d8324d8
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/ruby.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ruby.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ruby.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ruby.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ruby

Ruby 프로그래밍 언어 인터프리터.
같이 보기: `gem`, `bundler`, `rake`, `irb`.
더 많은 정보: <https://www.ruby-lang.org>.

- Ruby 스크립트 실행:

`ruby `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.rb</span>

- 명령줄에서 단일 Ruby 명령 실행:

`ruby -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 주어진 Ruby 스크립트에서 구문 오류 확인:

`ruby -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.rb</span>

- 현재 디렉토리에서 포트 8080으로 내장 HTTP 서버 시작:

`ruby -run -e httpd`

- 필요한 라이브러리를 설치하지 않고 로컬에서 Ruby 바이너리 실행:

`ruby -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라이브러리_폴더_경로</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라이브러리_요구_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이너리_폴더_경로/바이너리_이름</span>

- Ruby 버전 표시:

`ruby -v`
