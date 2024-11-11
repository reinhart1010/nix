---
layout: page
title: linux/steghide (한국어)
description: "JPEG, BMP, WAV 및 AU 파일 형식을 위한 스테가노그래피 도구."
content_hash: e5acc59db7f7d23053ca92aed76c3eb45d13f027
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/steghide.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/steghide.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># steghide

JPEG, BMP, WAV 및 AU 파일 형식을 위한 스테가노그래피 도구.
더 많은 정보: <https://github.com/StefanoDeVuono/steghide>.

- PNG에 데이터를 삽입하고 암호 구문을 입력받기:

`steghide embed --coverfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>` --embedfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터.txt</span>

- WAV 오디오 파일에서 데이터 추출:

`steghide extract --stegofile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소리.wav</span>

- 파일 정보 표시 및 삽입된 파일 탐지 시도:

`steghide info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jpg</span>

- JPEG 이미지에 최대 압축으로 데이터 삽입:

`steghide embed --coverfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpg</span>` --embedfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터.txt</span>` --compress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>

- 지원되는 암호화 알고리즘 및 모드 목록 확인:

`steghide encinfo`

- 예를 들어 Blowfish CBC 모드로 JPEG 이미지에 암호화된 데이터 삽입:

`steghide embed --coverfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.jpg</span>` --embedfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터.txt</span>` --encryption `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blowfish|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cbc|...</span>
