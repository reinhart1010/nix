---
layout: page
title: common/git-bugreport (한국어)
description: "시스템 및 사용자로부터 디버그 정보를 수집하여 Git 버그 보고에 도움이 되는 텍스트 파일을 생성합니다."
content_hash: 94936fb2cbca258fc7d009d76f792894a88c1917
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-bugreport.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-bugreport.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bugreport.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git bugreport

시스템 및 사용자로부터 디버그 정보를 수집하여 Git 버그 보고에 도움이 되는 텍스트 파일을 생성합니다.
더 많은 정보: <https://git-scm.com/docs/git-bugreport>.

- 현재 디렉토리에 새로운 버그 보고 파일 생성:

`git bugreport`

- 지정된 디렉토리에 새로운 버그 보고 파일 생성 (디렉토리가 없을 경우 생성됨):

`git bugreport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output-directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- `strftime` 형식의 지정된 파일명 접미사를 사용하여 새로운 버그 보고 파일 생성:

`git bugreport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--suffix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%m%d%y</span>
