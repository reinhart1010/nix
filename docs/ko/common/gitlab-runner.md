---
layout: page
title: common/gitlab-runner (한국어)
description: "GitLab 실행기 관리."
content_hash: eded089c38a7015c3009528d84f7d605a3a3a0a5
last_modified_at: 2024-10-23
related_topics:
  - title: English version
    url: /en/common/gitlab-runner.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/gitlab-runner.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gitlab-runner.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gitlab-runner

GitLab 실행기 관리.
더 많은 정보: <https://docs.gitlab.com/runner/>.

- 실행기 등록:

`sudo gitlab-runner register --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://gitlab.example.com</span>` --registration-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- Docker 실행기로 실행기를 등록:

`sudo gitlab-runner register --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://gitlab.example.com</span>` --registration-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --executor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker</span>

- 실행기 등록 해제:

`sudo gitlab-runner unregister --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 실행기 서비스 상태릂 표시:

`sudo gitlab-runner status`

- 실행기 서비스를 다시 시작:

`sudo gitlab-runner restart`

- 등록된 실행기가 GitLab에 연결할 수 있는지 확인:

`sudo gitlab-runner verify`
