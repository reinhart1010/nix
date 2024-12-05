---
layout: page
title: common/zipalign (中文)
description: "Zip 文件对齐工具。"
content_hash: 3503404aa6cf99e743342b70ea6c15b119d8430a
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zipalign.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zipalign.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zipalign

Zip 文件对齐工具。
是 Android 软件开发工具包构建工具的一部分。
更多信息：<https://developer.android.com/tools/zipalign>.

- 在 4 字节边界上对齐一个 Zip 文件的数据：

`zipalign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.zip</span>

- 检查一个 Zip 文件是否在 4 字节边界上正确对齐，并以详细的方式显示结果：

`zipalign -v -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入.zip</span>
