---
layout: page
title: linux/eyed3 (한국어)
description: "MP3 파일의 메타데이터를 읽고 조작합니다."
content_hash: f7ec6dfa605b7ef3cdb10dbe591b594a72fb1518
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/eyed3.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/eyed3.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eyeD3

MP3 파일의 메타데이터를 읽고 조작합니다.
더 많은 정보: <https://eyed3.readthedocs.io>.

- MP3 파일의 정보 보기:

`eyeD3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명.mp3</span>

- MP3 파일의 제목 설정:

`eyeD3 --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명.mp3</span>

- 폴더 내 모든 MP3 파일의 앨범 설정:

`eyeD3 --album "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앨범_이름</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.mp3</span>

- MP3 파일의 앞면 커버 이미지 설정:

`eyeD3 --add-image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앞면_커버.jpeg</span>`:FRONT_COVER: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명.mp3</span>
