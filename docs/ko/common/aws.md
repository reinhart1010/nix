---
layout: page
title: common/aws (한국어)
description: "Amazon Web Services의 공식 CLI tool입니다."
content_hash: e84fda01ccc5a07345d416a906d1100ad6e64d0f
related_topics:
  - title: Deutsch version
    url: /de/common/aws.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aws.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/aws.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws

Amazon Web Services의 공식 CLI tool입니다.
더 많은 정보: <https://aws.amazon.com/cli>.

- 모든 IAM 사용자 목록:

`aws iam list-users`

- 특정 지역의 모든 ec2 인스턴스 나열:

`aws ec2 describe-instances --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- 특정 SQS 대기열에서 메시지 수신:

`aws sqs receive-message --queue-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://queue.amazonaws.com/546123/Test</span>

- 특정 SNS 주제에 메시지 게시:

`aws sns publish --topic-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn:aws:sns:us-east-1:54633:testTopic</span>` --message "Message"`

- AWS 명령어에 대한 도움말을 보려면:

`aws `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` help`
