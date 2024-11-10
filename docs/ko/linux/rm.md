---
layout: page
title: linux/rm (한국어)
description: "파일 또는 디렉터리 삭제."
content_hash: 37b6313ab78f0a43f2e0465bec85f95ee8388891
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/rm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/rm.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rm

파일 또는 디렉터리 삭제.
같이 보기: `rmdir`.
더 많은 정보: <https://www.gnu.org/software/coreutils/rm>.

- 특정 파일 삭제:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 존재하지 않는 파일은 무시하고 특정 파일 삭제:

`rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 파일을 삭제하기 전에 대화형 메시지를 표시하여 특정 파일을 삭제:

`rm --interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 파일을 삭제하고 삭제한 파일 정보를 출력:

`rm --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 파일 및 디렉터리를 재귀적으로 삭제:

`rm --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>

- 빈 디렉토리 제거 (안전한 방법으로 간주됨):

`rm --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
