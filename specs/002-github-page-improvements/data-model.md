# Data Model: Improvement Suggestions for Jekyll GitHub Pages Site

## Entities

### 1. Popular Implementation
- **Attributes:**
  - name (string): Repository or site name
  - url (string): Link to the repository or site
  - stars (integer): GitHub stars (if applicable)
  - theme (string): Jekyll theme used
  - features (list of strings): Notable features or best practices
  - notes (string): Additional notes or context

### 2. Improvement Suggestion
- **Attributes:**
  - id (string/uuid): Unique identifier
  - title (string): Short summary of the suggestion
  - description (string): Detailed explanation
  - rationale (string): Why this is suggested
  - priority (enum: P1/P2/P3): Priority level
  - status (enum: proposed/applied/rejected): Current status
  - reference (url or text): Source or justification
  - dateSuggested (date): When the suggestion was made
  - dateApplied (date, optional): When the suggestion was applied

### 3. Changelog Entry
- **Attributes:**
  - improvementId (string): ID of the applied improvement
  - description (string): What was changed
  - dateApplied (date): When the change was made
  - userFeedback (string, optional): Feedback or results
  - impact (string, optional): Observed impact or metrics

## Relationships
- Each improvement suggestion may reference one or more popular implementations as inspiration or justification.
- Suggestions and changelog entries are tracked over time, with status updates and rationale for acceptance/rejection.

## Validation Rules
- Each suggestion must have a clear title, description, and rationale.
- Status must be one of: proposed, applied, rejected.
- Priority must be assigned (P1, P2, or P3).
- References must be valid URLs or documented sources.
