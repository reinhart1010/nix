---
layout: page
title: common/mp3info (한국어)
description: "MP3 파일의 ID3v1 태그를 보기/편집하는 도구(ID3v2는 지원하지 않음)."
content_hash: cae79114821d92abb03a1ceb83380fc7c58aeda4
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mp3info.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mp3info.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mp3info

MP3 파일의 ID3v1 태그를 보기/편집하는 도구(ID3v2는 지원하지 않음).
더 많은 정보: <https://www.ibiblio.org/mp3info>.

- 특정 MP3 파일의 모든 ID3v1 태그 표시:

`mp3info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mp3</span>

- ID3v1 태그를 대화식으로 편집:

`mp3info -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mp3</span>

- 특정 MP3 파일의 ID3v1 태그 값 설정:

`mp3info -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티스트_이름</span>`" -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노래_제목</span>`" -l "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앨범_제목</span>`" -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연도</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">댓글_텍스트</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mp3</span>

- 특정 MP3 파일의 앨범 내 트랙 번호 설정:

`mp3info -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트랙_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mp3</span>

- 유효한 장르와 해당 숫자 코드 목록 출력:

`mp3info -G`

- 특정 MP3 파일의 음악 장르 설정:

`mp3info -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장르_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mp3</span>
