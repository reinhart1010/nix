---
layout: page
title: common/qdbus (한국어)
description: "Inter-Process Communication (IPC) 및 Remote Procedure Calling (RPC) 메커니즘으로, 원래 Linux를 위해 개발되었습니다."
content_hash: dc500068cdc91e24e640c3a214d92df2ab070844
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/qdbus.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qdbus.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qdbus

Inter-Process Communication (IPC) 및 Remote Procedure Calling (RPC) 메커니즘으로, 원래 Linux를 위해 개발되었습니다.
더 많은 정보: <https://doc.qt.io/qt-5/qtdbus-index.html>.

- 사용 가능한 서비스 이름 나열:

`qdbus`

- 특정 서비스의 객체 경로 나열:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>

- 특정 객체에서 사용 가능한 메서드, 신호 및 속성 나열:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/대상/경로/객체</span>

- 인수를 전달하여 특정 메서드를 실행하고 반환된 값 표시:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/대상/경로/객체</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메서드_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수2</span>

- KDE Plasma 세션에서 현재 밝기 값 표시:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Solid.PowerManagement</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/org/kde/Solid/PowerManagement/Actions/BrightnessControl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Solid.PowerManagement.Actions.BrightnessControl.brightness</span>

- KDE Plasma 세션에서 특정 밝기 설정:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Solid.PowerManagement</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/org/kde/Solid/PowerManagement/Actions/BrightnessControl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>

- KDE Plasma 세션에서 볼륨 증가 단축키 호출:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.kglobalaccel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/component/kmix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">invokeShortcut</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">increase_volume</span>`"`

- 정상적으로 로그아웃한 후 아무것도 하지 않거나, 재부팅하거나, 종료:

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Shutdown</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Shutdown</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logout|logoutAndReboot|logoutAndShutdown</span>
