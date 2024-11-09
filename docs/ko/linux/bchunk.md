---
layout: page
title: linux/bchunk (한국어)
description: "CD 이미지를 `.iso` 및 `.cdr` 트랙 세트로 변환."
content_hash: 2de77aaf27a8c1f2648ae9be56d4ed4c6d66dae8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/bchunk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bchunk

CD 이미지를 `.iso` 및 `.cdr` 트랙 세트로 변환.
더 많은 정보: <http://he.fi/bchunk>.

- 바이너리 CD를 표준 iso9960 이미지 파일로 변환:

`bchunk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.bin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.cue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>

- 자세히 보기 모드로 변환:

`bchunk -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.bin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.cue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>

- 오디오 파일을 WAV 형식으로 출력:

`bchunk -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.bin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.cue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>
