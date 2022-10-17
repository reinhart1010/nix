---
layout: page
title: windows/chkdsk (தமிழ்)
description: "பிழைகளுக்கு கோப்பு முறைமை மற்றும் தொகுதி மெட்டாடேட்டாவைச் சரிபார்க்கவும்."
content_hash: 9ac66d9d9aa837c23e15dc215a105598a76f65bd
related_topics:
  - title: English version
    url: /en/windows/chkdsk.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/chkdsk.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/chkdsk.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chkdsk

பிழைகளுக்கு கோப்பு முறைமை மற்றும் தொகுதி மெட்டாடேட்டாவைச் சரிபார்க்கவும்.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- சரிபார்க்க டிரைவ் லெட்டர் (பெருங்குடல்), மவுண்ட் பாயிண்ட் அல்லது தொகுதி பெயரைக் குறிப்பிடவும்:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுதி</span>

- ஒரு குறிப்பிட்ட தொகுதியில் பிழைகளை சரிசெய்யவும்:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுதி</span>` /f`

- சரிபார்க்கும் முன் ஒரு குறிப்பிட்ட தொகுதியை இறக்கவும்:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுதி</span>` /x`

- பதிவு கோப்பு அளவை குறிப்பிட்ட அளவிற்கு மாற்றவும் (NTFS க்கு மட்டும்):

`chkdsk /l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அளவு</span>
