---
layout: page
title: common/git-bugreport (한국어)
description: "시스템 및 사용자로부터 디버그 정보를 수집하여 Git 버그 보고에 도움이 되는 텍스트 파일을 생성합니다."
content_hash: 021acadd4c3304d5716a36e16247d28c4bb17fb0
last_modified_at: 2024-10-07
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-bugreport.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git bugreport

시스템 및 사용자로부터 디버그 정보를 수집하여 Git 버그 보고에 도움이 되는 텍스트 파일을 생성합니다.
더 많은 정보: <https://git-scm.com/docs/git-bugreport>.

- 현재 디렉토리에 새로운 버그 보고 파일 생성:

`git bugreport`

- 지정된 디렉토리에 새로운 버그 보고 파일 생성 (디렉토리가 없을 경우 생성됨):

`git bugreport --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- `strftime` 형식의 지정된 파일명 접미사를 사용하여 새로운 버그 보고 파일 생성:

`git bugreport --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%m%d%y</span>
