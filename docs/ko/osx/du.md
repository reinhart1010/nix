---
layout: page
title: osx/du (한국어)
description: "디스크 사용량: 파일 및 폴더의 공간 사용량을 추정하고 요약합니다."
content_hash: e0d8ca04a480c4628b56a5b92b3b8400c55d4c19
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/du.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/osx/du.html
    icon: bi bi-globe
tldri18n_status: 2
---
# du

디스크 사용량: 파일 및 폴더의 공간 사용량을 추정하고 요약합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/du.1.html>.

- 지정된 단위(KiB/MiB/GiB)로 폴더와 모든 하위 폴더의 크기 나열:

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 사람이 읽기 쉬운 형식으로 폴더와 모든 하위 폴더의 크기 나열 (각 크기에 적합한 단위를 자동 선택):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 사람이 읽기 쉬운 단위로 단일 폴더의 크기 표시:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 폴더 및 그 내의 모든 파일과 폴더의 사람이 읽기 쉬운 크기 나열:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 사람이 읽기 쉬운 형식으로 폴더와 모든 하위 폴더의 크기를 N 레벨까지 나열:

`du -h -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 현재 폴더의 하위 폴더에 있는 모든 `.jpg` 파일의 사람이 읽기 쉬운 크기를 나열하고, 마지막에 누적 합계 표시:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
