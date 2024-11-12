---
layout: page
title: osx/ditto (한국어)
description: "파일 및 디렉토리를 복사합니다."
content_hash: 1bac896b3b68056b645b0b01c2b5f16fb88352be
last_modified_at: 2024-11-12
related_topics:
  - title: বাংলা version
    url: /bn/osx/ditto.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/ditto.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/ditto.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/ditto.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ditto

파일 및 디렉토리를 복사합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/ditto.1.html>.

- 원본 디렉토리의 내용을 대상 디렉토리의 내용으로 덮어쓰기:

`ditto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_폴더</span>

- 복사 중인 모든 파일에 대해 터미널 창에 한 줄씩 출력:

`ditto -V `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_폴더</span>

- 원본 파일 권한을 유지하면서 지정된 파일 또는 디렉토리 복사:

`ditto -rsrc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_폴더</span>
