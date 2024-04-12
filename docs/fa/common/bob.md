---
layout: page
title: common/bob (فارسی)
description: "مدیریت و جابجایی بین نسخه های مختلف Neovim."
content_hash: a958c3d2dce457333f3e7ee138c000eefe9e9c86
last_modified_at: 2024-04-12
related_topics:
  - title: English version
    url: /en/common/bob.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bob

مدیریت و جابجایی بین نسخه های مختلف Neovim.
اطلاعات بیشتر: <https://github.com/MordechaiHadad/bob>.

- نصب و جابجایی به نسخه خاصی از Neovim:

`bob use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nightly|stable|latest|version_string|commit_hash</span>

- فهرست نسخه های نصب شده و نسخه ای که اکنون استفاده می شود:

`bob list`

- حذف یک نسخه خاص از Neovim:

`bob uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nightly|stable|latest|version_string|commit_hash</span>

- حذف Neovim و پاک کردن هر تغییری که `bob` اعمال کرده است:

`bob erase`

- بازگشت به نسخه شبانه قبلی:

`bob rollback`
