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

1. **Contact form.** Submissions are sent in the background to Formspree, which emails them to consulting@datasphered.com. Set `FORMSPREE_ID` near the bottom of `contact.html` to your form ID (the part after `formspree.io/f/`). While it is empty, the form falls back to opening the visitor's email app with a pre-filled message. A hidden `_gotcha` field catches simple spam bots.
2. **Imagery.** Images are still hotlinked from static.wixstatic.com, so they will break if the Wix plan is cancelled. Run `python3 scripts/localise-images.py` once from the repo root to download them into `assets/img/` and rewrite the HTML, then commit.
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

## SEO and housekeeping

- `favicon.svg` is an adaptive (light/dark) version of the D mark.
- `robots.txt` and `sitemap.xml` are served from the root. Submit the sitemap in Google Search Console.
- Every page has a canonical URL and `og:url`; `404.html` is marked `noindex`.
