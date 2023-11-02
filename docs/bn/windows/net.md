---
layout: page
title: windows/net (বাংলা)
description: "সিস্টেম ইউটিলিটি যাতে নেটওয়ার্ক-সম্পর্কিত সেটিংস দেখা এবং পরিবর্তন করা হয়।"
content_hash: 17dcfd988131f6df93f71d06a3924f324b6a417f
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/windows/net.html
    icon: bi bi-globe
---
# net

সিস্টেম ইউটিলিটি যাতে নেটওয়ার্ক-সম্পর্কিত সেটিংস দেখা এবং পরিবর্তন করা হয়।
আরও তথ্য পাবেন: <https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)>।

- একটি Windows সার্ভিস সমকালিনভাবে চালু বা বন্ধ করুন:

`net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">শুরু|বন্ধ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">সার্ভিস</span>

- নিশ্চিত হোন একটি SMB শেয়ার বর্তমান কনসোলে উপলব্ধ:

`net use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\\smb_shared_folder</span>` /USER:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ব্যবহারকারীনাম</span>

- বর্তমানে SMB এর উপর ভাগ করা ফোল্ডারগুলি দেখান:

`net share`

- আপনার SMB শেয়ারগুলি ব্যবহার করছে কে তা দেখান (উচ্চতম কনসোলে চালান):

`net session`

- একটি স্থানীয় সিকিউরিটি গ্রুপে ব্যবহারকারীগুলি দেখান:

`net localgroup "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">অ্যাডমিনিস্ট্রেটরস</span>`"`

- একটি ব্যবহারকারীকে স্থানীয় সিকিউরিটি গ্রুপে যোগ করুন (উচ্চতম কনসোলে চালান):

`net localgroup "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">অ্যাডমিনিস্ট্রেটরস</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ব্যবহারকারীনাম</span>` /add`

- একটি সাবকমান্ডের জন্য সাহায্য দেখান:

`net help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">সাবকমান্ড</span>

- সাহায্য দেখান:

`net help`
