---
layout: page
title: common/crane-index-append (한국어)
description: "원격 인덱스에 매니페스트를 추가."
content_hash: d5444027b43ffe4b9e6a9e7d7ecbc346ead9da24
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/crane-index-append.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-index-append.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane index append

원격 인덱스에 매니페스트를 추가.
하위 명령은 매니페스트가 추가된 (선택사항) 기본 인덱스를 기반으로 인덱스를 푸시.
추가된 매니페스트의 플랫폼은 구성 파일에서 유추되거나 실행 불가능한 경우 생략.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_append.md>.

- 원격 인덱스에 매니페스트를 추가:

`crane index append`

- 기본 인덱스에 추가할 매니페스트에 대한 참조:

`crane index append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--manifest</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매니페스트_이름1 매니페스트_이름2 ...</span>

- 결과 이미지에 적용할 태그:

`crane index append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>

- 비어있는 기본 인덱스에는 OCI 대신 Docker 미디어 유형을 지정:

`crane index append --docker-empty-base`

- 인덱스 자체가 아닌 각 하위의 항목을 추가 (기본값 true):

`crane index append --flatten`

- 도움말 표시:

`crane index append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
