---
layout: page
title: linux/cryptsetup (中文)
description: "管理普通 dm-crypt 和 LUKS（Linux 统一密钥设置）加密卷。"
content_hash: 131f10e034659e2aefc8df38c3a92a5431317874
last_modified_at: 2023-10-31
related_topics:
  - title: English version
    url: /en/linux/cryptsetup.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cryptsetup

管理普通 dm-crypt 和 LUKS（Linux 统一密钥设置）加密卷。
更多信息：<https://gitlab.com/cryptsetup/cryptsetup/>.

- 初始化 LUKS 卷（覆盖分区上的所有数据）：

`cryptsetup luksFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- 打开 LUKS 卷并在 `/dev/mapper/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标</span> 创建解密映射：

`cryptsetup luksOpen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标</span>

- 删除已存在的映射：

`cryptsetup luksClose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标</span>

- 更改 LUKS 卷的口令：

`cryptsetup luksChangeKey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>
