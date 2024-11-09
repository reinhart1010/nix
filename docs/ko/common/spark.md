---
layout: page
title: common/spark (한국어)
description: "Laravel Spark 명령줄 도구."
content_hash: 92f0b16156733f0615acfb6687e3ba6735f558ed
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/spark.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/spark.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># spark

Laravel Spark 명령줄 도구.
더 많은 정보: <https://spark.laravel.com>.

- API 토큰 등록:

`spark register `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>

- 현재 등록된 API 토큰 표시:

`spark token`

- 새 Spark 프로젝트 생성:

`spark new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- Braintree 스텁과 함께 새 Spark 프로젝트 생성:

`spark new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` --braintree`

- 팀 기반 결제 스텁과 함께 새 Spark 프로젝트 생성:

`spark new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` --team-billing`
