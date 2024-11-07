---
layout: page
title: common/mh_metric (한국어)
description: "MATLAB 또는 Octave 코드의 코드 메트릭을 계산하고 적용."
content_hash: 8fc14ea4af2e5d357938a13562dd7d7774f942a4
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mh_metric.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mh_metric.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mh_metric

MATLAB 또는 Octave 코드의 코드 메트릭을 계산하고 적용.
더 많은 정보: <https://misshit.org>.

- 지정된 파일의 코드 메트릭 출력:

`mh_metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.m 경로/대상/파일2.m ...</span>

- 지정된 Octave 파일의 코드 메트릭 출력:

`mh_metric --octave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.m 경로/대상/파일2.m ...</span>

- 지정된 디렉터리의 코드 메트릭을 재귀적으로 출력:

`mh_metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 현재 디렉터리의 코드 메트릭 출력:

`mh_metric`

- 코드 메트릭 보고서를 HTML 또는 JSON 형식으로 출력:

`mh_metric --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>
