---
layout: page
title: common/mongoexport (한국어)
description: "MongoDB 인스턴스에 저장된 데이터를 JSON 또는 CSV 형식으로 내보내기."
content_hash: e55b07be5fc9e749b485e57e2bd122440c2ec63f
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/mongoexport.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mongoexport.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mongoexport

MongoDB 인스턴스에 저장된 데이터를 JSON 또는 CSV 형식으로 내보내기.
더 많은 정보: <https://docs.mongodb.com/database-tools/mongoexport/>.

- 컬렉션을 JSON 형식으로 `stdout`에 내보내기:

`mongoexport --uri=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연결_문자열</span>` --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컬렉션_이름</span>

- 쿼리에 맞는 지정된 컬렉션의 문서를 JSON 파일로 내보내기:

`mongoexport --db=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컬렉션_이름</span>` --query="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리_객체</span>`" --out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>

- 문서를 한 줄에 하나의 객체 대신 JSON 배열로 내보내기:

`mongoexport --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컬렉션_이름</span>` --jsonArray`

- 문서를 CSV 파일로 내보내기:

`mongoexport --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컬렉션_이름</span>` --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">csv</span>` --fields="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드1,필드2,...</span>`" --out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>

- 지정된 파일의 쿼리에 맞는 문서를 CSV 파일로 내보내고, 첫 번째 줄에 필드 이름 목록 생략:

`mongoexport --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컬렉션_이름</span>` --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">csv</span>` --fields="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드1,필드2,...</span>`" --queryFile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --noHeaderLine --out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>

- 문서를 사람이 읽을 수 있는 JSON 형식으로 `stdout`에 내보내기:

`mongoexport --uri=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">몽고DB_URI</span>` --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컬렉션_이름</span>` --pretty`

- 도움말 표시:

`mongoexport --help`
