---
layout: page
title: common/ia (한국어)
description: "`archive.org`와 상호작용하기 위한 커멘드라인 도구."
content_hash: 7399a8a32d6f59168aa90d14f10ac3349dcee852
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ia.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ia

`archive.org`와 상호작용하기 위한 커멘드라인 도구.
더 많은 정보: <https://archive.org/services/docs/api/internetarchive/cli.html>.

- API 키로 `ia`를 구성 (일부 기능은 이 단계 없이 작동하지 않음):

`ia configure`

- 하나 이상의 항목을 `archive.org`에 업로드:

`ia upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">식별자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --metadata="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mediatype:data</span>`" --metadata="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title:example</span>`"`

- `archive.org`에서 하나 이상의 항목을 다운로드:

`ia download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목</span>

- `archive.org`에서 하나 이상의 항목을 삭제:

`ia delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">식별자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- `archive.org`에서 검색하여, 결과를 JSON로 반환:

`ia search '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject:"subject" collection:collection</span>`'`
