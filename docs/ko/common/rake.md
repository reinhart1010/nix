---
layout: page
title: common/rake (한국어)
description: "Ruby용 Make와 유사한 프로그램."
content_hash: 106e4128950534c9cb66ec28535810fa1f7f233a
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rake

Ruby용 Make와 유사한 프로그램.
`rake`의 작업은 Rakefile에 지정됩니다.
더 많은 정보: <https://ruby.github.io/rake>.

- `default` Rakefile 작업 실행:

`rake`

- 특정 작업 실행:

`rake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업</span>

- 동시에 `n`개의 작업 병렬 실행 (기본값은 CPU 코어 수 + 4):

`rake --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- 특정 Rakefile 사용:

`rake --rakefile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Rakefile</span>

- 다른 디렉토리에서 `rake` 실행:

`rake --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
