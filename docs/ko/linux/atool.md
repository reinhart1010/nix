---
layout: page
title: linux/atool (한국어)
description: "다양한 형식의 압축 파일을 관리합니다."
content_hash: 8f77849faff84653df936213a895aa7dc45b36a3
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/atool.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/atool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atool

다양한 형식의 압축 파일을 관리합니다.
더 많은 정보: <https://www.nongnu.org/atool/>.

- Zip 압축 파일의 파일 목록 표시:

`atool --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축_파일.zip</span>

- tar.gz 압축 파일을 새로운 하위 디렉토리(또는 파일이 하나뿐인 경우 현재 디렉토리)에 풀기:

`atool --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축_파일.tar.gz</span>

- 두 개의 파일로 새로운 7z 압축 파일 생성:

`atool --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축_파일.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 현재 디렉토리의 모든 Zip 및 rar 압축 파일 추출:

`atool --each --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip *.rar</span>
