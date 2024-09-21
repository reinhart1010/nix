---
layout: page
title: common/aws-s3-mb (한국어)
description: "S3 버킷들을 생성."
content_hash: 9b960efcd9d5992faffeff69365278178570b54b
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/aws-s3-mb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-s3-mb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws s3 mb

S3 버킷들을 생성.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mb.html>.

- S3 버킷을 생성:

`aws s3 mb s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>

- 특정 지역에 S3 버킷 생성:

`aws s3 mb s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리전</span>

- 도움말 표시:

`aws s3 mb help`
