---
layout: page
title: common/androguard (中文)
description: "使用 python 编写的一款针对安卓应用的逆向工程工具。"
content_hash: e5e846ca6705f860fada499eba1f875df08b2fe7
related_topics:
  - title: English version
    url: /en/common/androguard.html
    icon: bi bi-globe
---
# androguard

使用 python 编写的一款针对安卓应用的逆向工程工具。
更多信息：<https://github.com/androguard/androguard>.

- 展示 Android manifest 清单文件：

`androguard axml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/至/应用.apk</span>

- 展示 app 元数据（版本和 app ID）：

`androguard apkid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/至/应用.apk</span>

- 反编译 Java 代码：

`androguard decompile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/至/应用.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/至/目录</span>
