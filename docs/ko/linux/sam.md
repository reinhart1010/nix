---
layout: page
title: linux/sam (한국어)
description: "AWS Serverless Application Model (SAM) CLI."
content_hash: e0403c36df903bc07ab984b91f5300f42effa667
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sam.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sam.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sam

AWS Serverless Application Model (SAM) CLI.
더 많은 정보: <https://github.com/awslabs/aws-sam-cli>.

- 서버리스 애플리케이션 초기화:

`sam init`

- 특정 런타임으로 서버리스 애플리케이션 초기화:

`sam init --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python3.7</span>

- SAM 애플리케이션 패키징:

`sam package`

- Lambda 함수 코드 빌드:

`sam build`

- 로컬에서 서버리스 애플리케이션 실행:

`sam local start-api`

- AWS SAM 애플리케이션 배포:

`sam deploy`
