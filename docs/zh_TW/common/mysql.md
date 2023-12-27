---
layout: page
title: common/mysql (中文 (繁體, 台灣))
description: "MySQL 命令列工具。"
content_hash: 4e0c7df2bba327a933967a5b4875b0afb2163be6
last_modified_at: 2023-12-27
related_topics:
  - title: English version
    url: /en/common/mysql.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mysql.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/mysql.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/mysql.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mysql.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mysql

MySQL 命令列工具。
更多資訊：<https://www.mysql.com/>.

- 與資料庫連線：

`mysql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">資料庫名稱</span>

- 與資料庫連線，系統將提示使用者輸入密碼：

`mysql -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">使用者名稱</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">資料庫名稱</span>

- 連線到另一台主機上的資料庫：

`mysql -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">資料庫主機</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">資料庫名稱</span>

- 透過 Unix 通訊端連接到資料庫：

`mysql --socket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sock 檔路徑</span>

- 執行腳本檔案（批次檔）中的 `SQL` 語句：

`mysql -e "source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sql 檔案</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">資料庫名稱</span>

- 用 `mysqldump` 建立的備份還原資料庫（系統將提示使用者輸入密碼）：

`mysql --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">使用者名稱</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">資料庫名稱</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sql 備份檔路徑</span>

- 從備份中恢復所有資料庫（系統將提示使用者輸入密碼）：

`mysql --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">使用者名稱</span>` --password < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sql 備份檔路徑</span>
