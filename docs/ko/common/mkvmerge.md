---
layout: page
title: common/mkvmerge (한국어)
description: "멀티미디어 스트림을 병합하고 추출."
content_hash: eeef4108014d0504c5b63e49f24263d19ee66f3e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mkvmerge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkvmerge

멀티미디어 스트림을 병합하고 추출.
더 많은 정보: <https://mkvtoolnix.download/doc/mkvmerge.html>.

- Matroska 파일 정보 표시:

`mkvmerge --identify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mkv</span>

- 특정 파일의 트랙 1에서 오디오 추출:

`mkvextract tracks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mkv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.webm</span>

- 특정 파일의 트랙 3에서 자막 추출:

`mkvextract tracks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mkv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/자막.srt</span>

- 파일에 자막 트랙 추가:

`mkvmerge --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.mkv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mkv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/자막.srt</span>
