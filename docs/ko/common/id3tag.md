---
layout: page
title: common/id3tag (한국어)
description: "MP3 파일의 ID3v1 및 ID3v2 태그를 읽고, 쓰고, 조작."
content_hash: c80da937ae40acf493a793cb32c2f5442d20ab75
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/id3tag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/id3tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# id3tag

MP3 파일의 ID3v1 및 ID3v2 태그를 읽고, 쓰고, 조작.
더 많은 정보: <https://manned.org/id3tag>.

- MP3 파일의 아티스트 및 노래 제목 태그 설정:

`id3tag --artist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티스트</span>` --song `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노래_제목</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mp3</span>

- 현재 디렉토리에 있는 모든 MP3 파일의 앨범 제목 설정:

`id3tag --album `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앨범</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.mp3</span>

- 도움말 표시:

`id3tag --help`
