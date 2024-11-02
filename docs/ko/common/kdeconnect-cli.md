---
layout: page
title: common/kdeconnect-cli (한국어)
description: "파일이나 텍스트를 장치에 공유하거나, 벨소리를 울리거나, 잠금을 해제하는 등 여러 작업을 수행하기 위해 KDE Connect를 사용하세요."
content_hash: e4f920fd43c1f57c3b3b64c57dadff4ff26e0d78
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/kdeconnect-cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kdeconnect-cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kdeconnect-cli

파일이나 텍스트를 장치에 공유하거나, 벨소리를 울리거나, 잠금을 해제하는 등 여러 작업을 수행하기 위해 KDE Connect를 사용하세요.
더 많은 정보: <https://kdeconnect.kde.org>.

- 모든 장치 나열:

`kdeconnect-cli --list-devices`

- 사용 가능한 장치(페어링되고 접근 가능한) 나열:

`kdeconnect-cli --list-available`

- 특정 장치와 페어링 요청, 장치 ID 지정:

`kdeconnect-cli --pair --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_ID</span>

- 장치의 벨소리를 울리기, 장치 이름 지정:

`kdeconnect-cli --ring --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_이름</span>`"`

- URL 또는 파일을 페어링된 장치와 공유, 장치 ID 지정:

`kdeconnect-cli --share `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|경로/대상/파일</span>` --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_ID</span>

- 선택적 첨부 파일과 함께 특정 번호로 SMS 보내기:

`kdeconnect-cli --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_이름</span>`" --send-sms "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`" --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">전화번호</span>` --attachment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 장치 잠금 해제:

`kdeconnect-cli --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_이름</span>`" --unlock`

- 특정 장치에서 키 입력 시뮬레이션:

`kdeconnect-cli --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_이름</span>`" --send-keys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>
