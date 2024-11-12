---
layout: page
title: osx/setfile (한국어)
description: "HFS+ 디렉터리 내 파일의 속성을 설정합니다."
content_hash: 279f1c23d8d177bff67153a3acb5815eb7b9504e
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/setfile.html
    icon: bi bi-globe
tldri18n_status: 2
---
# setfile

HFS+ 디렉터리 내 파일의 속성을 설정합니다.
더 많은 정보: <https://ss64.com/osx/setfile.html>.

- 특정 파일의 생성 날짜 설정:

`setfile -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MM/DD/YYYY HH:MM:SS</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 파일의 수정 날짜 설정:

`setfile -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MM/DD/YYYY HH:MM:SS</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 심볼릭 링크 파일의 수정 날짜 설정 (링크된 파일 자체는 아님):

`setfile -P -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MM/DD/YYYY HH:MM:SS</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>
