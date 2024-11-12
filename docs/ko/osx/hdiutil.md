---
layout: page
title: osx/hdiutil (한국어)
description: "디스크 이미지를 생성하고 관리하는 유틸리티."
content_hash: 58f0a87476e1c4dfb2f039e3945119d7b594d6f9
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/hdiutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/hdiutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hdiutil

디스크 이미지를 생성하고 관리하는 유틸리티.
더 많은 정보: <https://keith.github.io/xcode-man-pages/hdiutil.1.html>.

- 이미지를 마운트:

`hdiutil attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_파일</span>

- 이미지를 마운트 해제:

`hdiutil detach /Volumes/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_파일</span>

- 마운트된 이미지 목록 표시:

`hdiutil info`

- 디렉터리의 내용을 ISO 이미지로 생성:

`hdiutil makehybrid -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
