---
layout: page
title: common/gsutil (한국어)
description: "Google Cloud 스토리지 접근."
content_hash: 60b0dd50de4416884604d693164117c5abb5792b
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gsutil.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/gsutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gsutil

Google Cloud 스토리지 접근.
`gsutil`을 사용하여 광범위한 버킷 및 객체 관리 작업을 수행 가능.
더 많은 정보: <https://cloud.google.com/storage/docs/gsutil>.

- 로그인한 프로젝트의 모든 버킷을 나열:

`gsutil ls`

- 버킷의 객체를 나열:

`gsutil ls -r 'gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>`**'`

- 버킷에서 객체 다운로드:

`gsutil cp gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/save_location</span>

- 버킷에 객체 업로드:

`gsutil cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object_location</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지_버킷_이름</span>`/`

- 버킷의 객체 이름을 바꾸거나 객체를 이동:

`gsutil mv gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오래된_객체_이름</span>` gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_객체_이름</span>

- 로그인한 프로젝트에서 새로운 버킷을 생성:

`gsutil mb gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>

- 버킷을 삭제하고 버킷에 있는 모든 객체를 제거:

`gsutil rm -r gs://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>
