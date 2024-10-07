---
layout: page
title: common/git-filter-repo (한국어)
description: "Git 히스토리를 재작성하는 다목적 도구."
content_hash: 21f79d94349c3599ca613faf0329db9846a1a197
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-filter-repo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-filter-repo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git filter-repo

Git 히스토리를 재작성하는 다목적 도구.
같이 보기: `bfg`.
더 많은 정보: <https://github.com/newren/git-filter-repo>.

- 모든 파일에서 민감한 문자열 대체:

`git filter-repo --replace-text <(echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">찾을_문자열</span>`==>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체할_문자열</span>`')`

- 특정 폴더를 히스토리를 유지하면서 추출:

`git filter-repo --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 폴더를 히스토리를 유지하면서 제거:

`git filter-repo --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --invert-paths`

- 하위 폴더의 모든 파일을 한 단계 위로 이동:

`git filter-repo --path-rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더/:</span>
