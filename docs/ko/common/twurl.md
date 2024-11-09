---
layout: page
title: common/twurl (한국어)
description: "Twitter API에 특화된 Curl과 유사한 명령어."
content_hash: 2f155f567e8ef637b47b83b62aa16291a3cdc8a9
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/twurl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/twurl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># twurl

Twitter API에 특화된 Curl과 유사한 명령어.
더 많은 정보: <https://github.com/twitter/twurl>.

- Twitter 계정에 대한 접근을 승인:

`twurl authorize --consumer-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트위터_API_키</span>` --consumer-secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트위터_API_비밀</span>

- API 엔드포인트에 GET 요청 수행:

`twurl -X GET `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트위터_API_엔드포인트</span>

- API 엔드포인트에 POST 요청 수행:

`twurl -X POST -d '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">엔드포인트_파라미터</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트위터_API_엔드포인트</span>

- Twitter에 미디어 업로드:

`twurl -H "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트위터_업로드_URL</span>`" -X POST "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트위터_업로드_엔드포인트</span>`" --file "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/미디어.jpg</span>`" --file-field "media"`

- 다른 Twitter API 호스트에 접근:

`twurl -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트위터_API_URL</span>` -X GET `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트위터_API_엔드포인트</span>

- 요청한 리소스에 대한 별칭 생성:

`twurl alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스</span>
