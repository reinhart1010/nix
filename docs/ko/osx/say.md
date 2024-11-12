---
layout: page
title: osx/say (한국어)
description: "텍스트를 음성으로 변환."
content_hash: 53329d35fae972c303f2c96e687b9a57e710e967
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/say.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/say.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/say.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/say.html
    icon: bi bi-globe
tldri18n_status: 2
---
# say

텍스트를 음성으로 변환.
더 많은 정보: <https://keith.github.io/xcode-man-pages/say.1.html>.

- 문구를 소리내어 말하기:

`say "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">나는 자전거 타는 것을 좋아해.</span>`"`

- [f]파일을 소리내어 읽기:

`say --input-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명.txt</span>

- 사용자 지정 음성과 속도로 문구 말하기:

`say --voice=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">음성</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분당_단어_수</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">미안해 데이브, 그렇게 할 수 없어.</span>`"`

- 사용 가능한 음성 목록 나열 (다양한 언어로 말하는 음성):

`say --voice="?"`

- 폴란드어로 말하기:

`say --voice=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Zosia</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Litwo, ojczyzno moja!</span>`"`

- 음성 텍스트의 오디오 파일 생성:

`say --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명.aiff</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Here's to the Crazy Ones.</span>`"`
