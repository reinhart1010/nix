---
layout: page
title: linux/feedreader (한국어)
description: "GUI 데스크톱 RSS 클라이언트."
content_hash: c0493c18c30b1d42425aafa48c566328cdda3179
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/feedreader.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/feedreader.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># feedreader

GUI 데스크톱 RSS 클라이언트.
참고: FeedReader는 더 이상 유지 관리되지 않습니다.
더 많은 정보: <https://github.com/jangernert/FeedReader>.

- 읽지 않은 기사 수 출력:

`feedreader --unreadCount`

- 팔로우할 피드의 URL 추가:

`feedreader --addFeed=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">피드_url</span>

- 특정 기사 URL로 가져오기:

`feedreader --grabArticle=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기사_url</span>

- 특정 기사에서 모든 이미지 다운로드:

`feedreader --url=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">피드_url</span>` --grabImages=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기사_경로</span>

- URL에서 미디어 재생:

`feedreader --playMedia=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기사_url</span>
