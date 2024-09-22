---
layout: page
title: common/aws-s3-website (한국어)
description: "버킷의 웹사이트 구성 설정."
content_hash: 85dc83986c279c954a5bee3013cc38dacd63ae56
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-s3-website.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws s3 website

버킷의 웹사이트 구성 설정.
추가 정보: `aws s3`.
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/s3/website.html>.

- 버킷을 정적 웹 사이트로 구성:

`aws s3 website `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s3://버킷-이름</span>` --index-document `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>

- 웹 사이트에 대한 오류 페이지 구성:

`aws s3 website `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s3://버킷-이름</span>` --index-document `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` --error-document `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">error.html</span>
