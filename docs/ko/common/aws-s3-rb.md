---
layout: page
title: common/aws-s3-rb (한국어)
description: "비어있는 S3 버킷 삭제."
content_hash: 1e4d1f5079505bea2e1a6f04f2f90862109e3e77
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-s3-rb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws s3 rb

비어있는 S3 버킷 삭제.
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/s3/rb.html>.

- 비어있는 S3 버킷 삭제:

`aws s3 rb s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>

- S3 버킷 및 버전이 지정되지 않은 객체를 강제 삭제 (버전이 명시된 객체가 있는 경우 충돌 발생):

`aws s3 rb s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>` --force`
