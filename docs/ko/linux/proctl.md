---
layout: page
title: linux/proctl (한국어)
description: "프로젝트 라이선스 및 언어를 관리하고, 템플릿화된 라이선스 간 전환을 수행합니다."
content_hash: 2ba8afc213c1c3958b30c4c9539357415c14fc65
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/proctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/proctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/proctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># proctl

프로젝트 라이선스 및 언어를 관리하고, 템플릿화된 라이선스 간 전환을 수행합니다.
더 많은 정보: <https://github.com/HeCodes2Much/proctl>.

- 사용 가능한 라이선스 나열:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-ll|-list-licenses</span>

- 사용 가능한 언어 나열:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-lL|-list-languages</span>

- FZF 메뉴에서 라이선스 선택:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-pl|-pick-license</span>

- FZF 메뉴에서 언어 선택:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-pL|-pick-language</span>

- 현재 프로젝트에서 모든 라이선스 제거:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|-remove-license</span>

- 새 라이선스 템플릿 생성:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|-new-template</span>

- 템플릿에서 라이선스 삭제:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-R|-delete-license</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@라이선스_이름1 @라이선스_이름2 ...</span>

- 유용한 명령어 목록 표시:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|-help</span>
