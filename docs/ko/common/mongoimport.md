---
layout: page
title: common/mongoimport (한국어)
description: "JSON, CSV, 또는 TSV 파일의 내용을 MongoDB 데이터베이스로 가져오기."
content_hash: 8ef68440c659a47342d93879a059e2213942058a
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/mongoimport.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mongoimport

JSON, CSV, 또는 TSV 파일의 내용을 MongoDB 데이터베이스로 가져오기.
더 많은 정보: <https://docs.mongodb.com/database-tools/mongoimport/>.

- 특정 컬렉션에 JSON 파일 가져오기:

`mongoimport --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>` --uri=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mongodb_uri</span>` --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컬렉션_이름</span>

- CSV 파일을 가져와서 파일의 첫 번째 줄을 필드 이름으로 사용:

`mongoimport --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">csv</span>` --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>` --db=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` --collection=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컬렉션_이름</span>

- JSON 배열을 가져와서 각 요소를 별도의 문서로 사용:

`mongoimport --jsonArray --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>

- 특정 모드와 기존 문서를 일치시키는 쿼리를 사용하여 JSON 파일 가져오기:

`mongoimport --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>` --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delete|merge|upsert</span>` --upsertFields="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드1,필드2,...</span>`"`

- 별도의 CSV 파일에서 필드 이름을 읽고 빈 값의 필드를 무시하여 CSV 파일 가져오기:

`mongoimport --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">csv</span>` --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>` --fieldFile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/필드_파일.csv</span>` --ignoreBlanks`

- 도움말 표시:

`mongoimport --help`
