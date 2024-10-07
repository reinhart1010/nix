---
layout: page
title: common/git-mergetool (한국어)
description: "병합 충돌을 해결하기 위해 병합 충돌 해결 도구를 실행."
content_hash: 002de74cc765e6837d7ad5569b3c8cc5685314d9
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-mergetool.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-mergetool.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-mergetool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-mergetool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git mergetool

병합 충돌을 해결하기 위해 병합 충돌 해결 도구를 실행.
더 많은 정보: <https://git-scm.com/docs/git-mergetool>.

- 기본 병합 도구를 실행하여 충돌 해결:

`git mergetool`

- 유효한 병합 도구 나열:

`git mergetool --tool-help`

- 이름으로 식별된 병합 도구 실행:

`git mergetool --tool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tool_name</span>

- 병합 도구를 실행하기 전에 각 호출마다 묻지 않음:

`git mergetool --no-prompt`

- GUI 병합 도구를 명시적으로 사용 (설정 변수 `merge.guitool` 참조):

`git mergetool --gui`

- 일반 병합 도구를 명시적으로 사용 (설정 변수 `merge.tool` 참조):

`git mergetool --no-gui`
