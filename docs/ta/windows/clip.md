---
layout: page
title: windows/clip (தமிழ்)
description: "உள்ளீட்டு உள்ளடக்கத்தை விண்டோஸ் கிளிப்போர்டுக்கு நகலெடுக்கவும்."
content_hash: 56dd7a0c8665372a559dd2ffa8e8d1b5c073b468
related_topics:
  - title: English version
    url: /en/windows/clip.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/clip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/clip.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># clip

உள்ளீட்டு உள்ளடக்கத்தை விண்டோஸ் கிளிப்போர்டுக்கு நகலெடுக்கவும்.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/clip>.

- விண்டோஸ் கிளிப்போர்டுக்கு குழாய் கட்டளை வரி வெளியீடு:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` | clip`

- ஒரு கோப்பின் உள்ளடக்கங்களை விண்டோஸ் கிளிப்போர்டுக்கு நகலெடுக்கவும்:

`clip < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.ext</span>

- விண்டோஸ் கிளிப்போர்டுக்கு புதிய வரியுடன் உரையை நகலெடுக்கவும்:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஏதாவது உரை</span>` | clip`

- விண்டோஸ் கிளிப்போர்டுக்கு புதிய வரி இல்லாமல் உரையை நகலெடுக்கவும்:

`echo | set /p="ஏதாவது உரை" | clip`
