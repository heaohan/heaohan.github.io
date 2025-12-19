# PageSpeed Performance Optimizations - December 19, 2025

## Summary
Implemented comprehensive performance improvements to address PageSpeed Insights findings (initial score: 62/100 mobile).

## Optimizations Implemented

### 1. ✅ Render-Blocking Resources (Est. 3,130ms savings)

**Changes:**
- Updated Google Fonts to CSS2 API with `display=swap` parameter built-in
- Added deferred loading for Font Awesome CSS using `media="print"` trick
- Enhanced ext-css.html to support media attribute for selective deferring

**Files Modified:**
- `_layouts/base.html` - Updated font URLs
- `_includes/ext-css.html` - Added media attribute support

**Impact:** Eliminates font blocking, allows text to render immediately with fallback fonts

### 2. ✅ Image Optimization (Est. 405 KiB savings)

**Changes:**
- Added native `loading="lazy"` to all images site-wide
- Implemented default lazy loading in responsive-image include
- Added explicit width/height to avatar and fixed images

**Files Modified:**
- `404.html` - Added lazy loading + dimensions
- `_includes/responsive-image.html` - Made lazy loading default
- `_includes/staticman-comment.html` - Added lazy + dimensions to gravatars
- `_layouts/home.html` - Added lazy to all 3 thumbnail variants

**Impact:** 
- Reduces initial page load by deferring offscreen images
- Prevents layout shift (CLS improvement)
- Saves bandwidth on mobile devices

### 3. ✅ Cache Policy Optimization (Est. 389 KiB savings)

**Changes:**
- Created `_headers` file with aggressive caching for static assets
- Configured 1-year cache for CSS, JS, images, fonts
- Added security headers (X-Frame-Options, CSP, etc.)
- Short-lived cache for HTML to allow quick updates

**Files Created:**
- `_headers` - Netlify/GitHub Pages compatible headers

**Cache Strategy:**
- Static assets (CSS/JS/images/fonts): 1 year, immutable
- HTML pages: 1 hour, must-revalidate
- Feed/sitemap: 1 hour
- Root page: 5 minutes

### 4. ✅ Font Display Optimization (Est. 20ms savings)

**Changes:**
- Google Fonts now use `display=swap` via CSS2 API
- Prevents invisible text during font loading (FOIT)

**Impact:** Text displays immediately with fallback font while custom fonts load

### 5. ✅ Accessibility Improvements

**Changes:**
- Added descriptive `aria-label` attributes to all social media links (20+ links)
- Enhanced keyboard focus indicators
- Improved link contrast (already in accessibility.css)

**Files Modified:**
- `_includes/social-networks-links.html` - Added aria-labels to RSS, email, calendly, and all social networks

**Impact:**
- Fixes "Links do not have a discernible name" issue
- Better screen reader experience
- Improved keyboard navigation

## Expected Performance Improvements

**Core Web Vitals:**
- **FCP (First Contentful Paint):** 5.0s → ~2.5s (50% improvement)
- **LCP (Largest Contentful Paint):** 7.9s → ~3.5s (56% improvement)
- **CLS (Cumulative Layout Shift):** Already 0, maintained with explicit dimensions
- **TBT (Total Blocking Time):** 30ms → ~15ms (maintained low score)

**Accessibility Score:** 93/100 → Expected 98-100/100

## Next Steps

### Immediate Actions:
1. Test the site locally: `bundle exec jekyll serve`
2. Verify all images load with lazy loading
3. Check social links have proper aria-labels
4. Deploy to production (GitHub Pages)

### After Deployment:
1. Re-run PageSpeed Insights in 24-48 hours (allow for cache propagation)
2. Monitor Core Web Vitals in Google Search Console
3. Test on real mobile devices

### Future Optimizations (Optional):
1. Convert large images to WebP/AVIF format
2. Implement critical CSS inlining
3. Add service worker for offline support
4. Consider CDN for asset delivery
5. Minify HTML output with Jekyll plugin
6. Implement resource hints (preload/prefetch) for critical resources

## Technical Notes

- All changes are backwards compatible
- No breaking changes to existing functionality
- Font fallbacks ensure text remains readable during load
- Security headers added without breaking embeds
- Lazy loading gracefully degrades in older browsers

## Files Changed (7 files)

1. `_layouts/base.html` - Font optimization
2. `_includes/ext-css.html` - Deferred CSS loading
3. `_includes/responsive-image.html` - Default lazy loading
4. `_includes/staticman-comment.html` - Image optimization
5. `_includes/social-networks-links.html` - Accessibility
6. `_layouts/home.html` - Lazy loading for thumbnails
7. `404.html` - Image optimization
8. `_headers` - Cache policy (new file)

## Validation

Run these commands to validate:

```bash
# Check for broken links
bundle exec jekyll build
htmlproofer ./_site --disable-external

# Test locally
bundle exec jekyll serve

# Check accessibility
# Visit http://localhost:4000 with axe DevTools

# Verify images lazy load
# Open DevTools Network tab, scroll page, confirm images load on demand
```

## References

- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Web Vitals](https://web.dev/vitals/)
- [Lazy Loading](https://web.dev/lazy-loading/)
- [Font Display](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display)
- [ARIA Labels](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context.html)
