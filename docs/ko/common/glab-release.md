---
layout: page
title: common/glab-release (한국어)
description: "GitLab 배포 관맄."
content_hash: f866fd0a422a1ed75c3aa844c1df86618a2e58ff
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/glab-release.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/glab-release.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># glab release

GitLab 배포 관맄.
더 많은 정보: <https://glab.readthedocs.io/en/latest/release>.

- Gitlab 저장소의 릴리스 목록은 30개 항목으로 제한됨:

`glab release list`

- 특정 릴리스에 대한 정보 표시:

`glab release view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 새로운 배포 생성:

`glab release create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 특정 배포 삭제:

`glab release delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 특정 릴리스에서 리소스 다운로드:

`glab release download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 특정 릴리스에 리소스 업로드:

`glab release upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>
