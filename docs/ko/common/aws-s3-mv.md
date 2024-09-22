---
layout: page
title: common/aws-s3-mv (한국어)
description: "로컬 파일이나 S3 객체를 로컬로 또는 S3의 다른 위치로 이동."
content_hash: 7aca48d81a1047e4d161c4eca6f3aa8b57cd589b
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-s3-mv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws s3 mv

로컬 파일이나 S3 객체를 로컬로 또는 S3의 다른 위치로 이동.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mv.html>.

- 로컬에서 지정된 버킷으로 파일 이동:

`aws s3 mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로컬_파일</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원격_파일</span>

- 특정 S3 객체를 다른 버킷으로 이동:

`aws s3 mv s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름1</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름2</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표파일</span>

- 특정 S3 객체를 원래 이름을 유지하는 다른 버킷으로 이동:

`aws s3 mv s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름1</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름2</span>

- 도움말 표시:

`aws s3 mv help`
