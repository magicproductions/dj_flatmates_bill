# Flatmates Bill - Django Application

Flatmates Bill is a Django-based web application that simplifies the task of splitting bills between two flatmates. It
factors in the number of days each flatmate has spent in the house within a certain period and calculates each one's
share of the total bill.

![dj_flatmates_bill.jpg](core%2Fstatic%2Fimages%2Fdj_flatmates_bill.jpg)

## Features

- Adding details of each flatmate such as name and days spent in the house.
- Adding details about the bill, specifically the total amount and the period it covers.
- Calculates and displays the bill share for each flatmate.

## Models & Attributes

The application mainly consists of two models:

1. **Flatmate**: Represents a flatmate living in the flat. The main fields include:

    - `name`: A CharField to store the name of the flatmate.
    - `days_in_house`: An IntegerField to store the number of days the flatmate has stayed in the flat.
    - `pays`: A method to calculate the share of the bill for the flatmate.

2. **Bill**: Represents the bill to be shared. The main fields include:

    - `amount`: A FloatField to store the total amount of the bill.
    - `period`: A CharField to store the period the bill is for.

## Installation & Setup

To run this project, you need to have Python and Django installed on your system.

1. Clone the repository.

2. Navigate to the project folder.

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the Django server:

    ```bash
    python manage.py runserver
    ```

## Usage

Visit the home page of the application. Enter the details for two flatmates and the total amount of the bill. The
application will calculate
the share of the bill for each flatmate and display the result. A PDF of the bill can also be downloaded.

## License

This project is licensed under the MIT License. Please see the `LICENSE` file for more details.

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss the proposed change.
