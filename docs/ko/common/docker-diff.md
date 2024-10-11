---
layout: page
title: common/docker-diff (한국어)
description: "컨테이너의 파일 시스템에서 파일이나 디렉토리의 변경 사항을 검사."
content_hash: 9101059ff9d3bd35931eeb47030cc559c6c2fc3a
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/docker-diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-diff.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/docker-diff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-diff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker diff

컨테이너의 파일 시스템에서 파일이나 디렉토리의 변경 사항을 검사.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/diff/>.

- 컨테이너가 생성된 이후의 변경 사항 검사:

`docker diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너</span>

- 도움말 표시:

`docker diff --help`
