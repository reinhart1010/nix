---
layout: page
title: common/git-changelog (한국어)
description: "저장소 커밋 및 태그에서 변경 로그 보고서를 생성."
content_hash: eb1c243fa1f16a03f1811540471dabdc0cc767b9
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-changelog.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-changelog.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-changelog.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git changelog

저장소 커밋 및 태그에서 변경 로그 보고서를 생성.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-changelog>.

- 최신 Git 태그 이후의 커밋 메시지로 기존 파일을 업데이트하거나 새 `History.md` 파일을 생성:

`git changelog`

- 현재 버전의 커밋 나열:

`git changelog --list`

- `2.1.0` 태그부터 현재까지의 커밋 범위 나열:

`git changelog --list --start-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.1.0</span>

- `0.5.0` 태그와 `1.0.0` 태그 사이의 커밋 범위를 보기 좋게 나열:

`git changelog --start-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5.0</span>` --final-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>

- 커밋 `0b97430`과 태그 `1.0.0` 사이의 커밋 범위를 보기 좋게 나열:

`git changelog --start-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0b97430</span>` --final-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>

- 출력 파일로 `CHANGELOG.md` 지정:

`git changelog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CHANGELOG.md</span>

- 현재 변경 로그 파일의 내용을 완전히 교체:

`git changelog --prune-old`
