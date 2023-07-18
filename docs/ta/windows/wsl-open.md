---
layout: page
title: windows/wsl-open (தமிழ்)
description: "பயனரின் இயல்புநிலை விண்டோஸ் GUI பயன்பாட்டில் லினக்ஸ்க்கான விண்டோஸ் துணை அமைப்பிலிருந்து ஒரு கோப்பு அல்லது URL ஐத் திறக்கவும்."
content_hash: 73aa05e06cbc34d4094d12fe8319e56706cd46ab
last_modified_at: 2023-07-18
related_topics:
  - title: English version
    url: /en/windows/wsl-open.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># wsl-open

பயனரின் இயல்புநிலை விண்டோஸ் GUI பயன்பாட்டில் லினக்ஸ்க்கான விண்டோஸ் துணை அமைப்பிலிருந்து ஒரு கோப்பு அல்லது URL ஐத் திறக்கவும்.
மேலும் விவரத்திற்கு: <https://gitlab.com/4U6U57/wsl-open>.

- விண்டோஸ் எக்ஸ்ப்ளோரரில் தற்போதைய கோப்பகத்தைத் திறக்கவும்:

`wsl-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- விண்டோஸில் பயனரின் இயல்புநிலை இணைய உலாவியில் URL ஐத் திறக்கவும்:

`wsl-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- விண்டோஸில் பயனரின் இயல்புநிலை பயன்பாட்டில் ஒரு குறிப்பிட்ட கோப்பைத் திறக்கவும்:

`wsl-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை\டு\கோப்பு</span>

- ஷெல்லின் இணைய உலாவியாக `wsl-open` ஐ அமைக்கவும் (`wsl-open` உடன் இணைப்புகளைத் திறக்கவும்):

`wsl-open -w`

- உதவியைக் காட்டு:

`wsl-open -h`
