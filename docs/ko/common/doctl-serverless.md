---
layout: page
title: common/doctl-serverless (한국어)
description: "서버리스 함수 관리."
content_hash: 550794c495e2ca8552ad15e7b4d583210dfdc0bd
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/doctl-serverless.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doctl-serverless.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doctl serverless

서버리스 함수 관리.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/serverless/>.

- 로컬 서버리스 지원을 함수 네임스페이스에 연결:

`doctl serverless connect`

- 함수 네임스페이스에 함수 프로젝트를 배포:

`doctl serverless deploy`

- 함수 프로젝트의 메타데이터 얻기:

`doctl serverless get-metadata`

- 서버리스 지원에 대한 정보를 제공:

`doctl serverless status`
