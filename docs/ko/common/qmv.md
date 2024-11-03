---
layout: page
title: common/qmv (한국어)
description: "기본 텍스트 편집기를 사용하여 파일 및 디렉터리의 이름을 정의하여 이동."
content_hash: d59cdc3581696ec3fd5c9a48f9f4d21a4428f8a3
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/qmv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qmv

기본 텍스트 편집기를 사용하여 파일 및 디렉터리의 이름을 정의하여 이동.
더 많은 정보: <https://www.nongnu.org/renameutils/>.

- 단일 파일 이동 (편집기를 열고 왼쪽에는 원본 파일 이름, 오른쪽에는 대상 파일 이름 표시):

`qmv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원본_파일</span>

- 여러 JPEG 파일 이동:

`qmv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- 여러 디렉터리 이동:

`qmv -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리3</span>

- 디렉터리 내의 모든 파일 및 디렉터리 이동:

`qmv --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 파일을 이동하되, 편집기에서 원본과 대상 파일 이름의 위치를 바꾸기:

`qmv --option swap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- 현재 디렉터리의 모든 파일 및 폴더 이름 변경, 편집기에서 대상 파일 이름만 표시 (단순 모드로 생각할 수 있음):

`qmv --format=do .`
