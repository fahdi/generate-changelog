# Git Changelog Generator 

This project generates a changelog page for a project and adds it to an existing HTML file that displays the daily changelog.

## Features

- Generate an HTML changelog page containing a list of changes.
- Add the changelog to an existing HTML file that displays the daily changelog.
- Retrieve the commit log for the project using the `subprocess` module and Git.
- Automatically format the changelog based on the type of change (added, changed, or removed).

## Dependencies

- Python 3.x
- Git

## Usage

To use the script, follow these steps:

1. Clone the repository to your local machine.
2. Copy the python code
2. Navigate to the any project directory in a terminal. It has to be a root directory for `git` so the script can do it's job. 
3. Run the following command in the terminal to generate the changelog: `python generate_changelog.py`. The changelog will be generated in an HTML file and it will be added to the `daily_changelog.html` file.
4. Open the `daily_changelog.html` file and make necessary edits if needed. 

## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.