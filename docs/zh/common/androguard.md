---
layout: page
title: common/androguard (中文)
description: "使用 Python 编写的一款针对安卓应用的逆向工程工具。"
content_hash: dc33621f3b97ba6b7377db2e58b10cff5ed54177
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/androguard.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/androguard.html
    icon: bi bi-globe
tldri18n_status: 2
---
# androguard

使用 Python 编写的一款针对安卓应用的逆向工程工具。
更多信息：<https://github.com/androguard/androguard>.

- 展示 Android manifest 清单文件：

`androguard axml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/至/应用.apk</span>

- 展示 app 元数据（版本和 app ID）：

`androguard apkid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/至/应用.apk</span>

- 反编译 Java 代码：

`androguard decompile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/至/应用.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/至/目录</span>
