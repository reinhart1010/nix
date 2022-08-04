---
layout: page
title: common/detox (한국어)
description: "작업하기 쉽도록 파일 이름을 다시 설정합니다."
content_hash: 7465f4383e7b585a29bcc7b9a2d9a97d0f0e1879
related_topics:
  - title: English version
    url: /en/common/detox.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/detox.html
    icon: bi bi-globe
---
# detox

작업하기 쉽도록 파일 이름을 다시 설정합니다.
그것은 공백과 다른 중복된 밑줄 문자같은 골칫거리들을 제거한다.
더 많은 정보: <https://github.com/dharple/detox>.

- 파일의 이름으로부터 공백과 다른 바람직하지 않은 문자들을 제거:

`detox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- detox가 디렉토리 트리에서 모든 파일 이름을 재설정하는 방법 출력:

`detox --dry-run -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리명</span>

- 디렉토리 트리에서 모든 파일들로부터 공백과 다른 바람직하지 않은 문자들을 제거:

`detox -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리명</span>
