---
layout: page
title: common/gcloud-kms-decrypt (한국어)
description: "Cloud KMS 키를 사용하여 암호화된 파일 복호화."
content_hash: dfe5500a96e0c7ab88f922349f5ef9ae8adcebfe
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gcloud-kms-decrypt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcloud kms decrypt

Cloud KMS 키를 사용하여 암호화된 파일 복호화.
같이 보기: `gcloud`.
더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/kms/decrypt>.

- 지정된 키, 키 링 및 위치를 사용하여 파일 복호화:

`gcloud kms decrypt --key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` --keyring=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_링_이름</span>` --location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>` --ciphertext-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호문</span>` --plaintext-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/평문</span>

- 추가 인증 데이터를 사용하여 파일을 복호화하고 복호화된 평문을 `stdout`에 출력:

`gcloud kms decrypt --key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` --keyring=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_링_이름</span>` --location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>` --additional-authenticated-data-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.aad</span>` --ciphertext-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호문</span>` --plaintext-file=-`
