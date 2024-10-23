---
layout: page
title: common/gitlab-ctl (한국어)
description: "GitLab 옴니버스를 관리."
content_hash: 45554d6ee25c7ca3e86d699e14fc1b6885decb8a
last_modified_at: 2024-10-23
related_topics:
  - title: English version
    url: /en/common/gitlab-ctl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/gitlab-ctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gitlab-ctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gitlab-ctl

GitLab 옴니버스를 관리.
더 많은 정보: <https://docs.gitlab.com/omnibus/maintenance/>.

- 모든 서비스의 상태를 표시:

`sudo gitlab-ctl status`

- 특정 서비스의 상태를 표시:

`sudo gitlab-ctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx</span>

- 모든 서비스 재시작:

`sudo gitlab-ctl restart`

- 특정 서비스 재시작:

`sudo gitlab-ctl restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx</span>

- 모든 서비스의 로그를 표시 및 `Ctrl + C`를 누를 때까지 계속 읽기:

`sudo gitlab-ctl tail`

- 특정 서비스의 로그를 표시:

`sudo gitlab-ctl tail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx</span>
