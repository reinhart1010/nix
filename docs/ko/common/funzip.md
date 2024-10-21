---
layout: page
title: common/funzip (한국어)
description: "추출 없이 아키이브의 첫 번째 (디렉토리가 아닌) 멤버의 내용을 출력."
content_hash: c1e98b642238fde1a838002c285c193235daf61b
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/funzip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# funzip

추출 없이 아키이브의 첫 번째 (디렉토리가 아닌) 멤버의 내용을 출력.
더 많은 정보: <https://manned.org/funzip>.

- Zip 아카이브의 첫 번째 멤버 내용을 출력:

`funzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>

- gzip 아카이브의 콘텐츠를 출력:

`funzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.gz</span>

- Zip 또는 gzip 아카이브를 해독하고 콘텐츠를 출력:

`funzip -password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브</span>
