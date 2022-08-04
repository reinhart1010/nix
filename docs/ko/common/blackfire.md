---
layout: page
title: common/blackfire (한국어)
description: "PHP용 커맨드라인 프로파일링 도구."
content_hash: d78591bcb5550505b72d100dbd200c50e8761f55
related_topics:
  - title: English version
    url: /en/common/blackfire.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/blackfire.html
    icon: bi bi-globe
---
# blackfire

PHP용 커맨드라인 프로파일링 도구.
더 많은 정보: <https://blackfire.io>.

- Blackfire 클라이언트 초기화 및 구성:

`blackfire config`

- Blackfire agent 시작:

`blackfire agent`

- 특정 소켓에서 Blackfire agent 시작:

`blackfire agent --socket="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp://127.0.0.1:8307</span>`"`

- 특정 프로그램에서 프로파일러 실행:

`blackfire run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.php/의/php 경로</span>

- 프로파일러 실행 및 샘플 10개 수집:

`blackfire --samples=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.php/의/php 경로</span>

- 프로파일러 및 출력 결과를 JSON으로 실행:

`blackfire --json run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.php/의/php 경로</span>

- 프로파일러 파일을 Blackfire 웹 서비스에 업로드:

`blackfire upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일/의/경로</span>

- Blackfire 웹 서비스에서 프로필 상태 확인:

`blackfire status`
