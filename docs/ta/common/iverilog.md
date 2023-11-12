---
layout: page
title: common/iverilog (தமிழ்)
description: "வெரிலாக் HDL (IEEE-1364) குறியீட்டை உருவகப்படுத்துதலுக்காக இயங்கக்கூடிய நிரல்களாக முன்செயலாக்கி தொகுக்கிறது."
content_hash: d339bd26845eb99c40dd0474f4afd6ce680f3f2f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/iverilog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iverilog

வெரிலாக் HDL (IEEE-1364) குறியீட்டை உருவகப்படுத்துதலுக்காக இயங்கக்கூடிய நிரல்களாக முன்செயலாக்கி தொகுக்கிறது.
மேலும் விவரத்திற்கு: <https://github.com/steveicarus/iverilog>.

- ஒரு மூல கோப்பை இயங்கக்கூடியதாக தொகுக்கவும்:

`iverilog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல.v</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/செயல்படுத்தக்கூடியது</span>

- அனைத்து எச்சரிக்கைகளையும் காண்பிக்கும் போது ஒரு மூலக் கோப்பை இயங்கக்கூடியதாக தொகுக்கவும்:

`iverilog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல.v</span>` -Wall -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/செயல்படுத்தக்கூடியது</span>

- VVP இயக்க நேரத்தைப் பயன்படுத்தி வெளிப்படையாக தொகுத்து இயக்கவும்:

`iverilog -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/செயல்படுத்தக்கூடியது</span>` -tvvp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல.v</span>

- வேறொரு பாதையிலிருந்து வெரிலாக் நூலகக் கோப்புகளைப் பயன்படுத்தி தொகுக்கவும்:

`iverilog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல.v</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/செயல்படுத்தக்கூடியது</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/நூலகம்_கோப்பகம்</span>

- தொகுக்காமல் வெரிலாக் குறியீட்டை முன்கூட்டியே செயலாக்கவும்:

`iverilog -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல.v</span>
