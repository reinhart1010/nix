---
layout: page
title: common/doctl-apps (한국어)
description: "DigitalOcean 앱 관리."
content_hash: ac6cd120d3072aef7f628f4ead91ab2bb31f50ed
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/doctl-apps.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doctl-apps.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doctl apps

DigitalOcean 앱 관리.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/apps>.

- 애플리케이션 생성:

`doctl apps create`

- 특정 애플리케이션에 대한 배포 생성:

`doctl apps create-deployment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>

- 대화형으로 앱 삭제:

`doctl apps delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>

- 앱 다운로드:

`doctl apps get`

- 모든 앱 나열:

`doctl apps list`

- 특정 앱의 모든 배포를 나열:

`doctl apps list-deployments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>

- 특정 앱에서 로그를 가져오기:

`doctl apps logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>

- 특정 앱 사양으로 특정 앱을 업데이트:

`doctl apps update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>` --spec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/spec.yml</span>
