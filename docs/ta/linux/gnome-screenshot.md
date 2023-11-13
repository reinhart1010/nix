---
layout: page
title: linux/gnome-screenshot (தமிழ்)
description: "திரை, சாளரம் அல்லது பயனர் வரையறுக்கப்பட்ட பகுதியைப் படம்பிடித்து, படத்தை ஒரு கோப்பில் சேமிக்கவும்."
content_hash: 602bee1cc307c61cfab1d06d274e3cda18e09db1
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/linux/gnome-screenshot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gnome-screenshot

திரை, சாளரம் அல்லது பயனர் வரையறுக்கப்பட்ட பகுதியைப் படம்பிடித்து, படத்தை ஒரு கோப்பில் சேமிக்கவும்.
மேலும் விவரத்திற்கு: <https://manned.org/gnome-screenshot>.

- ஒரு ஸ்கிரீன் ஷாட்டை எடுத்து இயல்புநிலை இடத்தில் சேமிக்கவும், பொதுவாக `~/Pictures`(படங்கள்):

`gnome-screenshot`

- ஒரு ஸ்கிரீன்ஷாட்டை எடுத்து, பெயரிடப்பட்ட கோப்பு இடத்தில் சேமிக்கவும்:

`gnome-screenshot --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>

- ஒரு ஸ்கிரீன்ஷாட்டை எடுத்து கிளிப்போர்டில் சேமிக்கவும்:

`gnome-screenshot --clipboard`

- குறிப்பிட்ட எண்ணிக்கையிலான வினாடிகளுக்குப் பிறகு ஸ்கிரீன்ஷாட்டை எடுக்கவும்:

`gnome-screenshot --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- க்னோம் ஸ்கிரீன்ஷாட் GUI ஐ துவக்கவும்:

`gnome-screenshot --interactive`

- தற்போதைய சாளரத்தின் ஸ்கிரீன்ஷாட்டை எடுத்து குறிப்பிட்ட கோப்பு இடத்தில் சேமிக்கவும்:

`gnome-screenshot --window --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>

- குறிப்பிட்ட வினாடிகளுக்குப் பிறகு ஸ்கிரீன் ஷாட்டை எடுத்து கிளிப்போர்டில் சேமிக்கவும்:

`gnome-screenshot --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --clipboard`

- பதிப்பைக் காட்டு:

`gnome-screenshot --version`
