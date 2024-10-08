---
layout: page
title: common/git-check-ignore (한국어)
description: "Git ignore/exclude (\".gitignore\") 파일을 분석하고 디버깅."
content_hash: e851176a1aacd0582be564cd86dc4ee65bcbafa9
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-check-ignore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-check-ignore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-check-ignore.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-check-ignore.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-check-ignore.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-check-ignore.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-check-ignore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git check-ignore

Git ignore/exclude (".gitignore") 파일을 분석하고 디버깅.
더 많은 정보: <https://git-scm.com/docs/git-check-ignore>.

- 파일 또는 폴더가 무시되는지 확인:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 여러 파일 또는 폴더가 무시되는지 확인:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>

- 각 경로를 한 줄씩 `stdin`에서 사용:

`git check-ignore --stdin < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_목록</span>

- 색인을 확인하지 않음 (경로가 추적되고 무시되지 않은 이유를 디버그하는 데 사용):

`git check-ignore --no-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>

- 각 경로에 대한 일치하는 패턴에 대한 세부 정보 포함:

`git check-ignore --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>
