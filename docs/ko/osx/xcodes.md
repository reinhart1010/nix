---
layout: page
title: osx/xcodes (한국어)
description: "여러 Xcode 버전을 다운로드, 설치 및 관리."
content_hash: a3d8e6fea9d9ee40792e7c172c16dd28c8b917ab
last_modified_at: 2024-10-25
related_topics:
  - title: English version
    url: /en/osx/xcodes.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/xcodes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/xcodes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcodes

여러 Xcode 버전을 다운로드, 설치 및 관리.
같이 보기: `xcodes runtimes`.
더 많은 정보: <https://github.com/xcodesorg/xcodes>.

- 설치된 모든 Xcode 버전 나열:

`xcodes installed`

- 사용 가능한 모든 Xcode 버전 나열:

`xcodes list`

- 버전 번호 또는 경로를 지정하여 Xcode 버전 선택:

`xcodes select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcode_버전|경로/대상/Xcode.app</span>

- 특정 Xcode 버전 다운로드 및 설치:

`xcodes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcode_버전</span>

- 최신 Xcode 릴리스를 설치하고 선택:

`xcodes install --latest --select`

- 특정 Xcode 버전 아카이브를 주어진 디렉토리에 다운로드(설치하지 않음):

`xcodes download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcode_버전</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
