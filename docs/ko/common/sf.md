---
layout: page
title: common/sf (한국어)
description: "Salesforce 조직과 작업할 때 개발 및 빌드 자동화를 단순화하는 강력한 명령줄 인터페이스."
content_hash: fb6099b8e802ea81844f6c4bcc3114686875950e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sf

Salesforce 조직과 작업할 때 개발 및 빌드 자동화를 단순화하는 강력한 명령줄 인터페이스.
더 많은 정보: <https://developer.salesforce.com/tools/salesforcecli>.

- Salesforce 조직 승인:

`sf force:auth:web:login --setalias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>` --instanceurl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_URL</span>

- 승인된 모든 조직 나열:

`sf force:org:list`

- 기본 웹 브라우저에서 특정 조직 열기:

`sf force:org:open --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>

- 특정 조직에 대한 정보 표시:

`sf force:org:display --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>

- 소스 메타데이터를 조직에 푸시:

`sf force:source:push --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>

- 소스 메타데이터를 조직에서 가져오기:

`sf force:source:pull --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>

- 조직에 로그인한 사용자의 비밀번호 생성:

`sf force:user:password:generate --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>

- 조직에 로그인한 사용자에게 권한 세트 할당:

`sf force:user:permset:assign --permsetname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">권한_세트_이름</span>` --targetusername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>
