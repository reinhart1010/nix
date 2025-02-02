---
layout: page
title: common/git-cherry-pick (বাংলা)
description: "বিদ্যমান কমিট দ্বারা প্রবর্তিত পরিবর্তনগুলি বর্তমান ব্র্যাঞ্চে প্রয়োগ করুন।"
content_hash: 15746bad973ae9cbf0404f9afcbcaa090b5d264d
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-cherry-pick.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cherry-pick

বিদ্যমান কমিট দ্বারা প্রবর্তিত পরিবর্তনগুলি বর্তমান ব্র্যাঞ্চে প্রয়োগ করুন।
অন্য ব্র্যাঞ্চে পরিবর্তনগুলি প্রয়োগ করতে, প্রথমে পছন্দসই ব্র্যাঞ্চে স্যুইচ করতে `git checkout` ব্যবহার করুন।
আরও তথ্য পাবেন: <https://git-scm.com/docs/git-cherry-pick>।

- বর্তমান ব্র্যাঞ্চে কমিট করুন:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">কমিট</span>

- বর্তমান ব্র্যাঞ্চে বিভিন্ন ধরনের কমিট করুন (এছাড়াও দেখুন 'git rebase --onto`):

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">শুরুর_কমিট</span>`~..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">শেষের_কমিট</span>

- বর্তমান ব্র্যাঞ্চে  একাধিক (অ-ক্রমিক) কমিট  করুন:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">কমিট_১ কমিট_২ ...</span>

- কমিট তৈরি না করেই ওয়ার্কিং ডিরেক্টরিতে কমিটের পরিবর্তন যোগ করুন:

`git cherry-pick --no-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">কমিট</span>
