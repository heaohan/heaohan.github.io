# Quickstart: Applying GitHub Pages Best Practices

## 1. Review Research Findings
- See `research.md` for best practices and improvement opportunities.

## 2. Prioritize Suggestions
- Use the data model and contract to track suggestions.
- Focus on high-priority (P1) items first (e.g., performance, accessibility, SEO).

## 3. Apply Improvements
- Update `_config.yml`, `_includes/`, `_layouts/`, and `assets/` as needed.
- Optimize images and assets for performance.
- Add or improve meta tags, sitemap, and Open Graph for SEO.
- Audit and enhance accessibility (ARIA, color contrast, keyboard navigation).
- Integrate automated checks (HTMLProofer, Lighthouse, pa11y) if possible.

## 4. Track and Document Changes
- Record each applied suggestion in the tracking system (see contract and data-model).
- Update `README.md` or a dedicated changelog with improvements, user feedback, and their impact.

## 5. Test and Validate
- Manually test site on desktop and mobile.
- Run accessibility and performance audits.
- Ensure all changes are compatible with GitHub Pages and Beautiful Jekyll.

## 6. Deploy
- Use `bundle exec jekyll build` and `bundle exec jekyll serve` to preview locally.
- Push changes to GitHub to deploy.

---

For more details, see the full specification, data model, and research documents in this feature directory.

---

## Related Files

- Improvement suggestions and changelog: `suggestions.yaml`
- Research, best practices, and rationale: `research.md`
- Contract and data model: `contracts/improvement-suggestion.md`, `data-model.md`
