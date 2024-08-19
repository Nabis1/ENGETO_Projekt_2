# ENGETO_Projekt_2


## Description

This project is a set of automated tests for the Engeto website using the Playwright framework with pytest. The tests cover various functionalities of the website, including navigation, interaction with course details, and form submissions.

## Project Setup

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)
- `pytest`
- `pytest-playwright`
- Playwright dependencies

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Nabis1/ENGETO_Projekt_2.git
    cd ENGETO_Projekt_2
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt` file, you can manually install the dependencies:

    ```bash
    pip install pytest pytest-playwright
    ```

4. **Install Playwright browsers:**

    ```bash
    playwright install
    ```

### Running Tests

To run the tests, use the following command:

```bash
pytest
```

You can also run tests with specific options, such as --headed to see the browser in action or --slowmo to slow down test execution:

```bash
pytest --headed

pytest --slowmo=1000
```
