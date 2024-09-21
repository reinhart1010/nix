---
layout: page
title: common/aws-s3api (한국어)
description: "Amazon S3 버킷을 생성 및 삭제하고 버킷 속성을 편집."
content_hash: 9b3ee4db41e1913011e777da71f2fd23d3bcac92
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/aws-s3api.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-s3api.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws s3api

Amazon S3 버킷을 생성 및 삭제하고 버킷 속성을 편집.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html>.

- 특정 리전에 버킷 생성:

`aws s3api create-bucket --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리전</span>` --create-bucket-configuration LocationConstraint=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리전</span>

- 버킷 삭제:

`aws s3api delete-bucket --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>

- 버킷 나열:

`aws s3api list-buckets`

- 버킷 내부의 객체를 나열하고, 각 객체의 키와 크기만 표시:

`aws s3api list-objects --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>` --query '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Contents[].{Key: Key, Size: Size}</span>`'`

- 버킷에 객체를 추가:

`aws s3api put-object --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_key</span>` --body `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- 버킷에서 객체 다운로드 (출력 파일은 항상 마지막 인수로 와야 함):

`aws s3api get-object --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체_키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 지정된 버킷에 Amazon S3 버킷 정책 적용:

`aws s3api put-bucket-policy --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>` --policy file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/버킷_정책.json</span>

- 지정된 버킷에서 Amazon S3 버킷 정책 다운로드:

`aws s3api get-bucket-policy --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>` --query Policy --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|table|text|yaml|yaml-stream</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/버킷_정책</span>
