---
layout: page
title: common/aws-s3-presign (한국어)
description: "Amazon S3 객체에 대해 미리 서명된 URL 생성."
content_hash: e4ff5862b1937df7f6f9617cf8fcc11d20a1542c
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-s3-presign.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws s3 presign

Amazon S3 객체에 대해 미리 서명된 URL 생성.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html>.

- 한 시간 동안 유효한 특정 S3 객체에 대해 미리 서명된 URL을 생성:

`aws s3 presign s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 수명 동안 유효한 미리 서명된 URL을 생성:

`aws s3 presign s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --expires-in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지속_시간</span>

- 도움말 표시:

`aws s3 presign help`
