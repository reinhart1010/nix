---
layout: page
title: common/docker-secret (한국어)
description: "Docker 스웜 비밀 관리."
content_hash: ea0d6619b231838e8c10bc0f27a3fc67df16391e
last_modified_at: 2024-10-11
related_topics:
  - title: Deutsch version
    url: /de/common/docker-secret.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-secret.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-secret.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-secret.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-secret.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-secret.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker secret

Docker 스웜 비밀 관리.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/secret/>.

- `stdin`에서 새 비밀 생성:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀_이름</span>` -`

- 파일에서 새 비밀 생성:

`docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 모든 비밀 나열:

`docker secret ls`

- 하나 이상의 비밀에 대한 자세한 정보를 사람이 읽기 쉬운 형식으로 표시:

`docker secret inspect --pretty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀_이름1 비밀_이름2 ...</span>

- 하나 이상의 비밀 제거:

`docker secret rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀_이름1 비밀_이름2 ...</span>
