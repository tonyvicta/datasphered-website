# datasphered-website

Static rebuild of the Datasphere Dynamics website, migrated off Wix and hosted on Vercel.

## Structure

| File | Route |
| --- | --- |
| index.html | / |
| services.html | /services |
| industries.html | /industries |
| solutions.html | /solutions |
| technology-partners.html | /technology-partners |
| case-study-oracle-to-snowflake.html | /case-study-oracle-to-snowflake |
| vision.html | /vision |
| contact.html | /contact |
| legal-notice.html | /legal-notice |
| privacy-policy.html | /privacy-policy |
| cookie-policy.html | /cookie-policy |
| 404.html | not found page |
| styles.css | shared stylesheet |
| vercel.json | clean URLs, legacy Wix redirects, security headers |

Plain HTML and CSS. There is no build step, so Vercel should use the "Other" framework preset with no build command and the repository root as the output directory.

## Before go live

1. **Contact form.** `contact.html` posts to `https://formspree.io/f/REPLACE_WITH_YOUR_FORM_ID`. Create a free form endpoint (for example at formspree.io) and replace that ID, otherwise submissions go nowhere. The email and phone links work regardless.
2. **Imagery.** The original Wix pages used photographic and abstract background images. This rebuild uses CSS gradients instead. Download the originals from the Wix Media Manager, commit them to an `assets/` folder, and reference them if you want the exact look back.
3. **Logo.** The "D" mark is inlined as SVG in the header of each page. The wordmark is set in Montserrat rather than the original brand font.
4. **Legal pages.** The cookie policy previously referenced Wix as the platform. Those references were made generic. Review all three legal pages before publishing.
5. **Fonts.** Inter and Montserrat are loaded from Google Fonts. Swap in the real brand typefaces if you have licences for them.

## Local preview

Open `index.html` directly in a browser, or run a static server from the repository root:

```
python3 -m http.server 8000
```

Note that clean URLs such as `/services` only work on Vercel. Locally use `/services.html`.
# datasphered-website
Datasphere Dynamics website - static rebuild for Verel hosting
