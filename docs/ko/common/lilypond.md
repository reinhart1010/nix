---
layout: page
title: common/lilypond (한국어)
description: "악보를 조판하고/또는 파일에서 MIDI를 생성합니다."
content_hash: 7bc228a5f27b28dd6ca217a4449cdf4cd7b1a3d0
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lilypond.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lilypond

악보를 조판하고/또는 파일에서 MIDI를 생성합니다.
같이 보기: `musescore`.
더 많은 정보: <https://lilypond.org>.

- lilypond 파일을 PDF로 컴파일:

`lilypond `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정된 형식으로 컴파일:

`lilypond --formats=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">형식_덤프</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 진행 상태 업데이트를 생략하고 지정된 파일을 컴파일:

`lilypond -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정된 파일을 컴파일하고 출력 파일 이름 지정:

`lilypond --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>

- lilypond의 현재 버전 확인:

`lilypond --version`
