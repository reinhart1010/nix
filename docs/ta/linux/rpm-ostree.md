---
layout: page
title: linux/rpm-ostree (தமிழ்)
description: "ஒரு கலப்பின படம்/தொகுப்பு அமைப்பு."
content_hash: 1d8bd438b864d1d59c6fcce6c572f48a46216fae
related_topics:
  - title: English version
    url: /en/linux/rpm-ostree.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rpm-ostree

ஒரு கலப்பின படம்/தொகுப்பு அமைப்பு.
ostree வரிசைப்படுத்தல்கள், தொகுப்பு அடுக்குகள், கோப்பு முறைமை மேலடுக்குகள் மற்றும் துவக்க உள்ளமைவு ஆகியவற்றை நிர்வகிக்கவும்.
மேலும் விவரத்திற்கு: <https://coreos.github.io/rpm-ostree/administrator-handbook/>.

- துவக்க ஏற்றியில் தோன்றும் வரிசையில் `rpm-ostree` வரிசைப்படுத்தல்களைக் காட்டு:

`rpm-ostree status`

- காலாவதியான மற்றும் புதுப்பிக்கக்கூடிய தொகுப்புகளைக் காட்டு:

`rpm-ostree upgrade --preview`

- மேம்படுத்தப்பட்ட தொகுப்புகளுடன் ஒரு புதிய `ostree` வரிசைப்படுத்தலைத் தயாரித்து அதில் மீண்டும் துவக்கவும்:

`rpm-ostree upgrade --reboot`

- முந்தைய ostree வரிசைப்படுத்தலில் மீண்டும் துவக்கவும்:

`rpm-ostree rollback --reboot`

- ஒரு புதிய ostree வரிசைப்படுத்தலில் ஒரு தொகுப்பை நிறுவி அதில் மீண்டும் துவக்கவும்:

`rpm-ostree install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு</span>` --reboot`
