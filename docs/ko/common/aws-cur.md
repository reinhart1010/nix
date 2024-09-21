---
layout: page
title: common/aws-cur (한국어)
description: "AWS 사용 보고서 정의 파일 생성, 쿼리 및 삭제."
content_hash: 904478c625b95bb8f6510524004e56d05d145b52
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/aws-cur.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-cur.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-cur.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/common/aws-cur.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-cur.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-cur.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws cur

AWS 사용 보고서 정의 파일 생성, 쿼리 및 삭제.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>.

- JSON 파일에서 AWS 비용 및 사용 보고서 정의 파일 생성:

`aws cur put-report-definition --report-definition file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/리포트_정의파일.json</span>

- 로그인 한 계정에 대해 정의된 사용 보고서 정의 나열:

`aws cur describe-report-definitions`

- 사용 보고서 정의 삭제:

`aws cur --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_리전</span>` delete-report-definition --report-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포트</span>
