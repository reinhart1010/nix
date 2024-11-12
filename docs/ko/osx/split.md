---
layout: page
title: osx/split (한국어)
description: "파일을 여러 조각으로 분할합니다."
content_hash: 1804decec75c201a75d2f8d9a5932a17c21365a6
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/split.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/split.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/split.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/split.html
    icon: bi bi-globe
tldri18n_status: 2
---
# split

파일을 여러 조각으로 분할합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/split.1.html>.

- 파일을 각 조각이 10줄씩 되도록 분할 (마지막 조각 제외):

`split -l 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 정규 표현식으로 파일을 분할. 매칭된 라인은 다음 출력 파일의 첫 번째 라인이 됩니다:

`split -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat|^[dh]og</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각 조각이 512바이트가 되도록 파일을 분할 (마지막 조각 제외; 킬로바이트는 512k, 메가바이트는 512m 사용):

`split -b 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 5개의 파일로 분할. 각 조각은 동일한 크기를 가지도록 분할됩니다 (마지막 조각 제외):

`split -n 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
