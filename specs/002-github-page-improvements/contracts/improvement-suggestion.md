# Contract: Improvement Suggestion Tracking

## Purpose
Defines the format for tracking improvement suggestions for a Jekyll-based GitHub Pages site.

## Fields

## Example
```yaml
id: 001
title: "Optimize images for faster load times"
description: "Compress and resize images in assets/img/ to improve page speed."
rationale: "Large images slow down page loads and hurt performance scores."
priority: P1
status: applied
reference: "https://web.dev/fast/#optimize-your-images"
dateSuggested: 2026-03-29
dateApplied: 
```
# Changelog Entry Fields
- `improvementId`: ID of the applied improvement (string)
- `description`: What was changed (string)
- `dateApplied`: When the change was made (date)
- `userFeedback`: Feedback or results (string, optional)
- `impact`: Observed impact or metrics (string, optional)

# Changelog Example
improvementId: 001
description: "All images in assets/img/ were compressed and resized."
dateApplied: 2026-04-01
userFeedback: "Site loads noticeably faster on mobile."
impact: "Lighthouse performance score increased from 82 to 95."
