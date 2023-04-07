import subprocess
import re
import datetime

def create_changelog_page(changes):
    # Generate filename for the changelog page
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = f'changelog_{date}.html'

    # Create the HTML content for the changelog page
    content = f'''<!DOCTYPE html>
<html>
<head>
	<title>Changelog for {date}</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<style>
		body {{
			font-family: Arial, sans-serif;
			font-size: 16px;
			line-height: 1.5;
			color: #333;
		}}
		h1 {{
			font-size: 24px;
			font-weight: bold;
			margin-bottom: 20px;
		}}
		ul {{
			margin-top: 0;
			margin-bottom: 20px;
		}}
		li {{
			margin-bottom: 10px;
		}}
		.icon {{
			margin-right: 5px;
			font-size: 20px;
			vertical-align: middle;
		}}
		.added {{
			color: green;
		}}
		.changed {{
			color: blue;
		}}
		.removed {{
			color: red;
		}}
	</style>
</head>
<body>
	<h1>Changelog for {date}</h1>
	<ul>'''

    # Add each change to the HTML content
    for change in changes:
        icon = ''
        class_name = ''
        if change['type'] == 'added':
            icon = '<span class="icon added">&#x2714;</span>'
            class_name = 'added'
        elif change['type'] == 'changed':
            icon = '<span class="icon changed">&#x270E;</span>'
            class_name = 'changed'
        elif change['type'] == 'removed':
            icon = '<span class="icon removed">&#x2718;</span>'
            class_name = 'removed'
        content += f'<li class="{class_name}">{icon}{change["message"]}</li>'

    # Add closing tags to the HTML content
    content += '''</ul>
	<script>
		// Automatically scroll to the bottom of the page on load
		window.onload = function() {
			window.scrollTo(0, document.body.scrollHeight);
		}
	</script>
</body>
</html>'''

    # Write the content to a file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    # Return the filename
    return filename


def estimate_type(message):
    """
    Estimates the type of change based on the commit message.

    Args:
        message (str): The commit message.

    Returns:
        str: The estimated type of change ('added', 'changed', or 'removed').
    """
    # Define keywords and phrases for each type of change
    added_keywords = ['add', 'new', 'create']
    changed_keywords = ['update', 'improve', 'modify', 'refactor']
    removed_keywords = ['remove', 'delete']

    # Check the commit message for each type of change
    for keyword in added_keywords:
        if keyword in message.lower():
            return 'added'
    for keyword in changed_keywords:
        if keyword in message.lower():
            return 'changed'
    for keyword in removed_keywords:
        if keyword in message.lower():
            return 'removed'

    # If no type of change is detected, return 'changed' as a default
    return 'changed'


# Define the regex pattern to extract the commit message and date
pattern = r'^([\w\s]+)\s([\d-]+)'

# Get the commit log from Git
log = subprocess.check_output(['git', 'log', '--pretty=format:%s %ad', '--date=format:%Y-%m-%d'])

# Split the log into individual commit messages
commits = log.decode('utf-8').split('\n')

# Extract the commit message and date from each commit
changes = []
for commit in commits:
    match = re.match(pattern, commit)
    if match:
        message = match.group(1)
        date = datetime.datetime.strptime(match.group(2), '%Y-%m-%d')
        changes.append({
            'type': estimate_type(message),
            'message': message,
            'date': date
        })

# Call the create_changelog_page function with the list of changes
filename = create_changelog_page(changes)

# Print the filename of the generated changelog file
print(f'Changelog file created: {filename}')    
