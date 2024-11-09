---
layout: page
title: common/slackcat (한국어)
description: "파일 및 명령 출력을 Slack에 전달하는 도구."
content_hash: 3103d6c0853b8e3de688b8079dd840b54df4708c
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/slackcat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/slackcat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># slackcat

파일 및 명령 출력을 Slack에 전달하는 도구.
더 많은 정보: <https://github.com/bcicen/slackcat>.

- 파일을 Slack에 게시:

`slackcat --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">채널_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 사용자 지정 파일 이름으로 파일을 Slack에 게시:

`slackcat --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">채널_이름</span>` --filename=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 명령 출력을 텍스트 스니펫으로 Slack에 파이프:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | slackcat --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">채널_이름</span>` --filename=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스니펫_이름</span>

- 명령 출력을 Slack에 지속적으로 스트리밍:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | slackcat --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">채널_이름</span>` --stream`
