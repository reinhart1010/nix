---
layout: page
title: common/a2ping (한국어)
description: "이미지를 EPS 또는 PDF 파일로 변환."
content_hash: fad3d74b40f558eba90c312b8f1dacf30500a1c3
last_modified_at: 2023-11-03
related_topics:
  - title: বাংলা version
    url: /bn/common/a2ping.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/a2ping.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/a2ping.html
    icon: bi bi-globe
---
# a2ping

이미지를 EPS 또는 PDF 파일로 변환.
더 많은 정보: <https://manned.org/a2ping>.

- 이미지를 PDF로 변환 (참고: 출력 파일 이름 지정은 선택사항):

`a2ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.pdf</span>

- 지정된 방법을 사용해 문서를 압축:

`a2ping --nocompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|zip|best|flate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- HiResBoundingBox가 있는 경우 검색 (참고: 기본값은 yes):

`a2ping --nohires `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 원본 아래 및 왼쪽 페이지 콘텐츠 허용 (참고: 기본값은 no):

`a2ping --below `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `gs에 추가 인수 전달:

`a2ping --gsextra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 외부 프로그램 (예, pdftops)에 추가 인수 전달:

`a2ping --extra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 도움말 표시:

`a2ping -h`
