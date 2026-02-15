# Contribution Guidelines

To contribute a project or feature, you should only need to make changes to `projects.json`.

## Steps

1. Make changes to `projects.json` (take note of the [project structure](#project-data-structure))

2. Re-generate the README.md file:

  ```bash
  python generate_table.py
  ```

3. Submit your pull request

## Files

For more involved contributions a description of the main project files are:

- **`projects.json`**: Contains all projects and their features
- **`readme.tpl`**: Template file for the README (contains static content and `{{COMPARISON_TABLE}}` placeholder)
- **`generate_table.py`**: Python script that generates the table from JSON and validates its integrity
- **`readme.md`**: Generated output file (the main README)
- **`features.md`**: Feature definitions and descriptions

## Project Data Structure

The `projects.json` file contains two main sections:

### 1. Projects Array

Each project requires these **mandatory fields**:
- `name`: Project name
- `repo`: GitHub repository (owner/repo format)
- `logo_url`: URL to project logo
- `logo_alt`: Alt text for logo

**Optional standard fields**:
- `branch`: Branch name (defaults to "master" for badges)
- `license_custom`: Custom license text (overrides GitHub badge)

**Feature fields**: Any feature defined in the features array can be added as:
- `feature_name`: Value indicating the quality of the feature on a scale of 1-10 ("x" means the feature doesn't exist, and prepending 'wip-' means feature is a work in process)
- `feature_name_url`: Optional URL to link to the project's documentation of the feature

Example:
```json
{
  "name": "ProjectName",
  "repo": "owner/repo",
  "branch": "main",
  "logo_url": "https://...",
  "logo_alt": "Project Logo",
  "web_app": "8",
  "web_app_url": "https://demo.example.com",
  "voice_chat": "7",
  "encryption": "x",
  "encryption_url": "https://github.com/owner/repo/issues/123"
  ...
}
```

### 2. Features Array

Each feature defines a row in the comparison table:

```json
{
  "name": "Feature Name",
  "link": "features.md#feature-anchor",
  "processor": "generate_default_row"
}
```

**Processor Types**:
- `generate_logo_row`: Special processor for logo display
- `generate_badge_row`: GitHub badge generation (requires badge_template, use_lowercase, use_branch)
- `generate_license_row`: License badge handling
- `generate_default_row` (or null): Score-based row with emoji conversion

### Score Value Conversion

The system automatically converts score values to an emoji representation:
- `"x"` → ❌ (not available)
- `"0"-"9"` → ✅0️⃣-✅9️⃣ (available with rating)
- `"10"` → ✅🔟 (perfect score - used sparingly)
- `"wip-1"` → 🚧1️⃣ (work in progress with rating of 1)

### Adding New Features

To add a new feature:

1. Add the feature definition to the `features` array in `projects.json`
2. Add descriptions to `features.md`
3. Add the feature scores to each project in the `projects` array
4. Regenerate the README

### Data Validation

The script validates that all required fields are present and feature scores are valid.