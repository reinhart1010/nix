---
layout: page
title: linux/pw-metadata (한국어)
description: "PipeWire 객체의 메타데이터를 모니터링, 설정 및 삭제."
content_hash: cee08caa1070f278d53854e609b867090702603b
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/pw-metadata.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/pw-metadata.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-metadata.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-metadata

PipeWire 객체의 메타데이터를 모니터링, 설정 및 삭제.
같이 보기: `pipewire`, `pw-mon`, `pw-cli`.
더 많은 정보: <https://docs.pipewire.org/page_man_pw-metadata_1.html>.

- `default` 이름의 메타데이터 표시:

`pw-metadata`

- `settings`에서 ID 0의 메타데이터 표시:

`pw-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">settings</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>

- 사용 가능한 모든 메타데이터 객체 나열:

`pw-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>

- 실행을 유지하며 메타데이터 변경 사항 기록:

`pw-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--monitor</span>

- 모든 메타데이터 삭제:

`pw-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>

- `settings`에서 `log.level`을 1로 설정:

`pw-metadata --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">settings</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">log.level</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 도움말 표시:

`pw-metadata --help`
