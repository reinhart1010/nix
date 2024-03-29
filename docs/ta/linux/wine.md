---
layout: page
title: linux/wine (தமிழ்)
description: "UNIX அடிப்படையிலான கணினிகளில் விண்டோஸ் இயங்குதளங்களை இயக்கவும்."
content_hash: d94adb25371cbc85a3c35507bf772fea3826b7e8
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/linux/wine.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wine

UNIX அடிப்படையிலான கணினிகளில் விண்டோஸ் இயங்குதளங்களை இயக்கவும்.
மேலும் விவரத்திற்கு: <https://wiki.winehq.org/>.

- `wine` சூழலில் ஒரு குறிப்பிட்ட நிரலை இயக்கவும்:

`wine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>

- பின்னணியில் ஒரு குறிப்பிட்ட நிரலை இயக்கவும்:

`wine start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>

- ஒரு MSI தொகுப்பை நிறுவவும்/நிறுத்தவும்:

`wine msiexec /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i|x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்போ/அடைவோ/நிரல்தொகுப்பு.msi</span>

- `கோப்பு எக்ஸ்ப்ளோரர்`, `நோட்பேட்` அல்லது `வேர்ட்பேட்` ஐ இயக்கவும்:

`wine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">explorer|notepad|write</span>

- `ரெஜிஸ்ட்ரி எடிட்டர்`, `கண்ட்ரோல் பேனல்` அல்லது `டாஸ்க் மேனேஜர்` ஆகியவற்றை இயக்கவும்:

`wine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regedit|control|taskmgr</span>

- கட்டமைப்பு கருவியை இயக்கவும்:

`wine winecfg`
