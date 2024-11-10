---
layout: page
title: common/trufflehog (한국어)
description: "파일, Git 저장소, S3 버킷 및 Docker 이미지에서 인증 정보를 찾고 검증."
content_hash: b135bee913272a52d71e54fce6fd73e288b9fda1
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/trufflehog.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/trufflehog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# trufflehog

파일, Git 저장소, S3 버킷 및 Docker 이미지에서 인증 정보를 찾고 검증.
더 많은 정보: <https://github.com/trufflesecurity/trufflehog>.

- Git 저장소에서 검증된 비밀 검색:

`trufflehog git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/trufflesecurity/test_keys</span>` --only-verified`

- GitHub 조직에서 검증된 비밀 검색:

`trufflehog github --org=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trufflesecurity</span>` --only-verified`

- GitHub 저장소에서 검증된 키 검색 및 JSON 출력 받기:

`trufflehog git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/trufflesecurity/test_keys</span>` --only-verified --json`

- GitHub 저장소와 그 이슈 및 풀 리퀘스트 검색:

`trufflehog github --repo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/trufflesecurity/test_keys</span>` --issue-comments --pr-comments`

- S3 버킷에서 검증된 키 검색:

`trufflehog s3 --bucket=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷 이름</span>` --only-verified`

- IAM 역할을 사용하여 S3 버킷 검색:

`trufflehog s3 --role-arn=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iam-role-arn</span>

- 개별 파일 또는 디렉터리 검색:

`trufflehog filesystem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리1 경로/대상/파일_또는_디렉터리2 ...</span>

- Docker 이미지에서 검증된 비밀 검색:

`trufflehog docker --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trufflesecurity/secrets</span>` --only-verified`
