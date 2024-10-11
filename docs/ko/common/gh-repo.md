---
layout: page
title: common/gh-repo (한국어)
description: "GitHub 저장소 작업."
content_hash: 216ded2ece4854fe33aad19842ccd81c1bfe329f
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gh-repo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gh-repo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-repo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh repo

GitHub 저장소 작업.
더 많은 정보: <https://cli.github.com/manual/gh_repo>.

- 새 저장소 생성 (저장소 이름이 설정되지 않으면, 기본 이름은 현재 디렉토리 이름이 됨):

`gh repo create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 저장소 복제:

`gh repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>

- 저장소 포크 및 복제:

`gh repo fork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>` --clone`

- 기본 웹 브라우저에서 저장소 보기:

`gh repo view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>` --web`

- 특정 사용자 또는 조직이 소유한 저장소 나열 (소유자가 설정되지 않으면, 기본 소유자는 현재 로그인된 사용자):

`gh repo list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>

- 포크가 아닌 저장소만 나열하고 나열할 저장소 수 제한 (기본값: 30):

`gh repo list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>` --source -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제한</span>

- 특정 주요 코딩 언어가 있는 저장소 나열:

`gh repo list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>` --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어_이름</span>
