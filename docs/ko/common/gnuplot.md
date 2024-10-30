---
layout: page
title: common/gnuplot (한국어)
description: "다양한 포맷으로 출력하는 그래프 플로터."
content_hash: 366d1d3ede28012d789a6e3c90c239981113638b
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/gnuplot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gnuplot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gnuplot

다양한 포맷으로 출력하는 그래프 플로터.
더 많은 정보: <http://www.gnuplot.info/>.

- 대화형 그래프 플로팅 쉘을 시작:

`gnuplot`

- 지정된 그래프 정의 파일에 대한 그래프를 그림:

`gnuplot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/정의파일.plt</span>

- 정의 파일을 로드하기 전에 명령을 실행하여 출력 형식을 설정:

`gnuplot -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set output "경로/대상/파일이름.png" size 1024,768</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/정의파일.plt</span>

- gnuplot이 종료된 후에도 그래프 플롯 미리보기 창을 유지:

`gnuplot --persist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/정의파일.plt</span>
