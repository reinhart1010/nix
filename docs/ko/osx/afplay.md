---
layout: page
title: osx/afplay (한국어)
description: "명령줄 오디오 플레이어."
content_hash: 045b28ee77f498e461b81bf145fe666208f584c3
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/afplay.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/afplay.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/afplay.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/afplay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# afplay

명령줄 오디오 플레이어.
더 많은 정보: <https://keith.github.io/xcode-man-pages/afplay.1.html>.

- 사운드 파일 재생 (재생이 끝날 때까지 대기):

`afplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 사운드 파일을 2배속으로 재생 (재생 속도):

`afplay --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 사운드 파일을 반속도로 재생:

`afplay --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 사운드 파일의 처음 N초만 재생:

`afplay --time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
