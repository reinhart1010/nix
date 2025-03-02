---
layout: page
title: common/aws-s3-rm (한국어)
description: "S3 객체 삭제."
content_hash: 0294144e8c706fa51bace5aa309f4fc49ac7699a
last_modified_at: 2024-11-27
related_topics:
  - title: English version
    url: /en/common/aws-s3-rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws s3 rm

S3 객체 삭제.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/rm.html>.

- 특정 S3 객체 삭제:

`aws s3 rm s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 S3 객체를 삭제하지 않고 삭제 결과를 미리보기 (dry-run):

`aws s3 rm s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --dryrun`

- 특정 S3 액세스 포인트에서 객체 삭제:

`aws s3 rm s3://arn:aws:s3:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리전</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정_아이디</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">액세스_포인트</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">액세스_포인트_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체_키</span>

- 버킷 내 모든 객체 삭제 (버킷 비우기):

`aws s3 rm s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>` --recursive`

- 도움말 표시:

`aws s3 rm help`
