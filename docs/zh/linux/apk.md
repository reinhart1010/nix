---
layout: page
title: linux/apk (中文)
description: "Alpine Linux 的包管理工具。"
content_hash: 93eb542a8dc23c27c83bd0f91ffaa5b793e23ff2
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/apk.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apk.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apk.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apk

Alpine Linux 的包管理工具。
更多信息：<https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- 从所有的远程仓库中更新仓库索引：

`apk update`

- 安装一个新软件包：

`apk add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 移除一个软件包：

`apk del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 修复或更新软件包而不修改主依赖项：

`apk fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 通过关键字查找软件包：

`apk search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键字</span>

- 获取指定软件包的相关信息：

`apk info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>
