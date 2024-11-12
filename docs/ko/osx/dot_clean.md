---
layout: page
title: osx/dot_clean (한국어)
description: "._* 파일을 해당 기본 파일과 병합합니다."
content_hash: ca10006653b6b723314c61752e522a49be516737
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/dot_clean.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/dot_clean.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/dot_clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dot_clean

._* 파일을 해당 기본 파일과 병합합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/dot_clean.1.html>.

- 모든 `._*` 파일을 재귀적으로 병합:

`dot_clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 디렉터리 내 모든 `._*` 파일을 재귀적으로 병합하지 않음 (단일 병합):

`dot_clean -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 모든 `._*` 파일을 병합하고 삭제:

`dot_clean -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 일치하는 기본 파일이 있을 경우에만 `._*` 파일 삭제:

`dot_clean -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 심볼릭 링크를 따라감:

`dot_clean -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 자세한 출력 표시:

`dot_clean -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
