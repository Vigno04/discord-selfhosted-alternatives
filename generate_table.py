#!/usr/bin/env python3
"""
Generate README.md from template and JSON data.
This script reads projects.json and readme.tpl to create the comparison table.
"""

import json


def _escape_table_cell(text):
    """Escape characters that break markdown table cells."""
    return str(text).replace("|", "\\|").strip()


def _escape_markdown_title(text):
    """Escape text for markdown link title attributes."""
    return str(text).replace('"', r'\"').strip()


def score_to_emoji(score):
    """
    Map score strings to their visual representation with emojis.

    Args:
        score: Can be a string like "x", "wip-3", "8", or an integer

    Returns:
        String with appropriate emoji representation

    Examples:
        "x" → "❌"
        "wip-3" → "🚧3️⃣"
        "8" or 8 → "✅8️⃣"
        "10" or 10 → "✅🔟"
    """
    # Convert to string for consistent handling
    score_str = str(score).strip().lower()

    # Map for emoji numbers 0-10
    emoji_numbers = {
        "0": "0️⃣",
        "1": "1️⃣",
        "2": "2️⃣",
        "3": "3️⃣",
        "4": "4️⃣",
        "5": "5️⃣",
        "6": "6️⃣",
        "7": "7️⃣",
        "8": "8️⃣",
        "9": "9️⃣",
        "10": "🔟",
    }

    # Handle "x" - Cross
    if score_str == "x":
        return "❌"

    # Handle "wip-N" - Work in progress with number
    if score_str.startswith("wip-"):
        number = score_str.split("-")[1]
        emoji_num = emoji_numbers.get(number, number)
        return f"🚧{emoji_num}"

    # Handle "wip" - Work in progress without number
    if score_str == "wip":
        return "🚧"

    # Handle "ok" - OK status
    if score_str == "ok":
        return "✅"

    # Handle plain numbers - Just the number emoji
    if score_str.isdigit():
        emoji_num = emoji_numbers.get(score_str, score_str)
        return emoji_num

    # Return as-is if no pattern matches
    return score_str


def load_json(filepath="projects.json"):
    """Load project data from JSON file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_table_header(projects):
    """Generate the table header with project names."""
    header = "| Feature "
    separator = "| :------- "

    for project in projects:
        name = project["name"]
        repo = project["repo"]
        url = f"https://github.com/{repo}"
        header += f"| [{name}]({url}) "
        separator += "| " + "-" * (len(url) + len(name) + 4) + " "

    header += "|\n"
    separator += "|\n"

    return header + separator


def generate_logo_row(projects):
    """Generate the logo row."""
    row = "| Logo "

    for project in projects:
        logo_url = project["logo_url"]
        logo_alt = project["logo_alt"]
        cell = f'<img src="{logo_url}" style="width: 50px"  alt="{logo_alt}"/>'
        row += f"| {cell} "

    row += "|\n"
    return row


def generate_badge_row(
    feature_name,
    feature_link,
    projects,
    badge_template,
    use_lowercase=False,
    use_branch=False,
):
    """
    Generic function to generate a row with badges.

    Args:
        feature_name: Name of the feature (e.g., "Github Stars")
        feature_link: Link for the feature header (e.g., "features.md#github-stars")
        projects: List of projects
        badge_template: Format string for the badge URL. Use {repo} and {branch} as placeholders
        use_lowercase: Whether to lowercase the repo name
        use_branch: Whether to include branch in the badge URL
    """
    row = f"| [{feature_name}]({feature_link}) "

    for project in projects:
        repo = project["repo"].lower() if use_lowercase else project["repo"]

        if use_branch:
            branch = project.get("branch", "master")
            badge = badge_template.format(repo=repo, branch=branch)
        else:
            badge = badge_template.format(repo=repo)

        row += f"| {badge} "

    row += "|\n"
    return row


def generate_license_row(projects):
    """Generate license row."""
    row = "| [License](features.md#license) "

    for project in projects:
        if "license_custom" in project:
            # Custom license display
            custom = project["license_custom"]
            badge = f"![?](https://img.shields.io/static/v1?label=%20&message={custom}&color=orange)"
        else:
            repo = project["repo"]
            badge = f"![?](https://img.shields.io/github/license/{repo}?label=%20)"
        
        # Check for custom license URL
        if "license_url" in project:
            url = project["license_url"]
            badge = f"[{badge}]({url})"
        
        row += f"| {badge} "

    row += "|\n"
    return row


def generate_default_row(feature, projects):
    """
    Generate a default row for features without a custom processor.
    Uses score_to_emoji to convert values.
    Also checks for feature_key + '_url' to create links.
    """
    feature_name = feature["name"]
    feature_link = feature.get("link")
    feature_key = feature_name.lower().replace(" ", "_").replace("/", "_")
    feature_url_key = feature_key + "_url"

    # Build row header
    if feature_link:
        row = f"| [{feature_name}]({feature_link}) "
    else:
        row = f"| {feature_name} "

    # Add cells for each project
    for project in projects:
        # Try to find the feature value in the project
        value = project.get(feature_key, "❌")

        # Convert value using score_to_emoji if it's a simple value
        if isinstance(value, (str, int)):
            cell = score_to_emoji(value)
        else:
            cell = value

        # Special handling for ui_vote
        if feature_key == "ui_vote":
            anchor = project["name"].lower().replace(" ", "-").replace("/", "-")
            url = f"ui_comparison/ui_comparison.md#{anchor}"
            cell = f"[{cell}]({url})"

        # Check if there's a URL field for this feature (even for X/❌ to link to reason/issue)
        if feature_url_key in project and feature_key != "ui_vote":
            url = project[feature_url_key]
            cell = f"{cell} [🔗]({url})"

        # Check for notes/tooltip — renders an ⚠️ icon with a hover title
        notes = project.get("notes", {})
        feature_note = notes.get(feature_key)
        if feature_note:
            tooltip = _escape_markdown_title(feature_note)
            tooltip_target = feature_link if feature_link else "#"
            cell += f' [⚠️]({tooltip_target} "{tooltip}")'

        row += f"| {cell} "

    row += "|\n"
    return row


def generate_comparison_table(data):
    """Generate the complete comparison table dynamically based on features."""
    projects = data["projects"]
    features = data.get("features", [])

    # Generate header
    table = generate_table_header(projects)

    # Loop over features and generate each row
    for feature in features:
        processor_name = feature.get("processor")

        # Match processor name and call appropriate function
        match processor_name:
            case "generate_logo_row":
                table += generate_logo_row(projects)

            case "generate_badge_row":
                # Read badge configuration from feature
                feature_name = feature["name"]
                feature_link = feature.get("link")
                badge_template = feature.get("badge_template", "")
                use_lowercase = feature.get("use_lowercase", False)
                use_branch = feature.get("use_branch", False)

                table += generate_badge_row(
                    feature_name,
                    feature_link,
                    projects,
                    badge_template,
                    use_lowercase=use_lowercase,
                    use_branch=use_branch,
                )

            case "generate_license_row":
                table += generate_license_row(projects)

            case _:
                # Use default conversion for unknown or null processors
                table += generate_default_row(feature, projects)

    return table


def generate_ui_comparison_md(projects, output_file="ui_comparison/ui_comparison.md"):
    """Generate the UI comparison markdown file."""
    md = "# UI Comparison\n\n"
    md += "The preview / screenshots were taken directly from the linked repositories.\n"
    md += "If an image is no longer available or out of date, please create an [issue](https://github.com/Vigno04/discord-selfhosted-alternatives/issues) or a [PR](https://github.com/Vigno04/discord-selfhosted-alternatives/pulls).\n\n"

    for project in projects:
        name = project["name"]
        repo = project["repo"]
        repo_url = f"https://github.com/{repo}"
        author = repo.split("/")[0]

        md += f"## [{name}]({repo_url}) by {author}\n\n"
        md += f"[` 🔵 Get this Project `]({repo_url})\n\n"

        ui_images = project.get("ui_images", [])
        if ui_images:
            for i in range(0, len(ui_images), 2):
                pair = ui_images[i : i + 2]
                normalized_items = []

                for img in pair:
                    if isinstance(img, str):
                        image_url = img
                        description = "Preview"
                    elif isinstance(img, dict):
                        image_url = img.get("url", "")
                        description = img.get("description", "Preview")
                    else:
                        continue

                    description = _escape_table_cell(description) or "Preview"
                    alt_text = _escape_table_cell(f"{name} {description}").strip()
                    normalized_items.append(
                        {
                            "description": description,
                            "image_url": image_url,
                            "alt_text": alt_text,
                        }
                    )

                if not normalized_items:
                    continue

                while len(normalized_items) < 2:
                    normalized_items.append(
                        {"description": "", "image_url": "", "alt_text": ""}
                    )

                left, right = normalized_items

                md += f"| {left['description']} | {right['description']} |\n"
                md += "| --- | --- |\n"

                left_img = (
                    f'<img src="{left["image_url"]}" alt="{left["alt_text"]}" width="480" />'
                    if left["image_url"]
                    else ""
                )
                right_img = (
                    f'<img src="{right["image_url"]}" alt="{right["alt_text"]}" width="480" />'
                    if right["image_url"]
                    else ""
                )

                md += f"| {left_img} | {right_img} |\n\n"
        else:
            md += "No images taken for now\n\n"

        md += "---\n\n"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(md)


def validate_projects_json(data):
    """Validate the projects.json structure."""
    projects = data["projects"]
    features = data.get("features", [])

    # Collect all validation errors
    errors = []

    # Check for missing required fields
    required_fields = {"name", "repo", "logo_url", "logo_alt"}

    for project in projects:
        missing_fields = required_fields - project.keys()
        if missing_fields:
            errors.append(
                f"Project '{project.get('name', 'Unknown')}' is missing fields: {missing_fields}"
            )

    # Check for undocumented keys
    # Build standard keys (fields that don't need to be in features)
    standard_keys = {"name", "repo", "branch", "logo_url", "logo_alt", "license_custom", "ui_images", "notes"}

    # Build feature keys from features array
    feature_keys = set()
    for feature in features:
        feature_name = feature["name"].lower().replace(" ", "_").replace("/", "_")
        feature_keys.add(feature_name)
        # Also add _url variant
        feature_keys.add(f"{feature_name}_url")

    # Track which projects have which keys
    all_keys = set()
    project_key_map = {}
    for project in projects:
        project_name = project.get("name", "Unknown")
        for key in project.keys():
            all_keys.add(key)
            if key not in project_key_map:
                project_key_map[key] = []
            project_key_map[key].append(project_name)

    # Find unmapped keys
    unmapped_keys = all_keys - standard_keys - feature_keys

    if unmapped_keys:
        errors.append(
            f"Found {len(unmapped_keys)} project key(s) not mapped to any feature:"
        )
        for key in sorted(unmapped_keys):
            projects_with_key = project_key_map[key]
            errors.append(f"  • '{key}' in: {', '.join(projects_with_key)}")

    # If any errors were found, print them and raise exception
    if errors:
        print("projects.json validation FAILED:")
        for error in errors:
            print(error)
        raise ValueError(f"projects.json validation failed with {len(errors)} error(s)")


def generate_readme(
    template_file="readme.tpl", output_file="readme.md", json_file="projects.json"
):
    """Generate README.md from template and JSON data."""
    # Load data
    data = load_json(json_file)

    # Read template
    with open(template_file, "r", encoding="utf-8") as f:
        template = f.read()

    # Validate data
    validate_projects_json(data)

    # Generate table
    table = generate_comparison_table(data)

    # Generate UI comparison
    generate_ui_comparison_md(data["projects"])

    # Replace placeholder in template
    output = template.replace("{{COMPARISON_TABLE}}", table)

    # Write output
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output)


if __name__ == "__main__":
    generate_readme()
