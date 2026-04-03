
<!--
Sync Impact Report
Version change: 0.0.0 → 1.0.0
Modified principles: All (template → Code Quality, Testing Standards, User Experience Consistency, Performance Requirements)
Added sections: Additional Constraints, Development Workflow
Removed sections: None
Templates requiring updates: ✅ plan-template.md, ✅ spec-template.md, ✅ tasks-template.md
Follow-up TODOs: TODO(RATIFICATION_DATE): Set original ratification date if known
-->

# heaohan.github.io Constitution

## Core Principles

### I. Code Quality
All code MUST adhere to clear, consistent style guides and be reviewed before merging. Code must be readable, maintainable, and free of unnecessary complexity. Linting and formatting tools are required. Dead code and unused dependencies MUST be removed promptly.
**Rationale**: High code quality reduces defects, improves maintainability, and accelerates onboarding.

### II. Testing Standards
All features MUST include automated tests. Unit, integration, and regression tests are required for all critical paths. No code is merged without passing tests and meeting coverage thresholds. Manual testing is required for user-facing changes.
**Exception**: For static JS features in Jekyll sites, a minimal automated JS test is required for core logic, but full automated test coverage is not mandatory. Manual and accessibility testing are considered sufficient for UI-centric features. See plan.md for documented rationale.
**Rationale**: Rigorous testing ensures reliability, prevents regressions, and builds user trust. Exception for static JS is justified by simplicity and UI-centric nature.

### III. User Experience Consistency
User interfaces and interactions MUST be consistent across the site. All user-facing changes must be reviewed for accessibility, clarity, and adherence to established design patterns. Feedback mechanisms and error states must be clear and actionable.
**Rationale**: Consistent UX improves usability, accessibility, and user satisfaction.

### IV. Performance Requirements
All features MUST meet defined performance targets. Pages must load quickly, and resource usage must be optimized. Performance regressions are not permitted. Monitoring and profiling are required for major changes.
**Rationale**: Strong performance ensures a positive user experience and supports scalability.

## Additional Constraints
All code must be open source and compatible with the Beautiful Jekyll theme. Security best practices must be followed. Third-party dependencies must be regularly reviewed and updated.

## Development Workflow
All changes require code review and must pass all CI checks before merging. Feature branches must be up to date with master before PR approval. Documentation must be updated with all user-facing or architectural changes.

## Governance
This constitution supersedes all other practices. Amendments require documentation, review, and approval. All PRs and reviews must verify compliance with these principles. Versioning follows semantic versioning: MAJOR for breaking changes, MINOR for new principles, PATCH for clarifications. Compliance is reviewed quarterly.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): Set original ratification date if known | **Last Amended**: 2026-03-29
