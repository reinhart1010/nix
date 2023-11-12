---
layout: page
title: osx/drutil (中文)
description: "与 DVD 刻录机交互。"
content_hash: 1cd2cca9db734de2a1b038e72aa3852ae705418b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/drutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/drutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# drutil

与 DVD 刻录机交互。
更多信息：<https://ss64.com/osx/drutil.html>.

- 从驱动器中弹出磁盘：

`drutil eject`

- 将目录作为 iso9660 文件系统刻录到 DVD 上。完成后不验证和弹出：

`drutil burn -noverify -eject -iso9660`
