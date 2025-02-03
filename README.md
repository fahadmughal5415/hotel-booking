# Hotel Booking System

This project is a simple hotel booking system implemented in Python. It allows users to book hotels and optionally book a SPA service. The system validates credit card details and performs authentication before confirming the booking.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/fahadmughal5415/hotel-booking.git
    ```
2. Navigate to the project directory:
    ```bash
    cd hotel-booking
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:
    ```bash
    python main.py
    ```
2. Follow the prompts to enter the hotel ID, credit card details, and customer name.
3. Optionally, you can book a SPA service.

## Project Structure

- `main.py`: The main script containing the hotel booking logic.
- `hotels.csv`: CSV file containing hotel information.
- `cards.csv`: CSV file containing credit card information.
- `card_security.csv`: CSV file containing credit card security information.

## Classes

- `Hotel`: Represents a hotel and provides methods to check availability and book the hotel.
- `ReservationTicket`: Generates a reservation ticket for the hotel booking.
- `CreditCard`: Validates credit card details.
- `SecureCreditCard`: Extends `CreditCard` and adds authentication.
- `SPAReservationTicket`: Extends `ReservationTicket` to generate a SPA reservation ticket.

## Example

```plaintext
Enter the id of the hotel: 1
Enter the credit card number: 1234567890123456
Enter the expiration date (MM/YY): 12/23
Enter the credit card holder's name: John Doe
Enter the CVV: 123
Enter the name of the customer: John Doe
Do you want to book a SPA? (yes/no): yes
```

## License

This project is licensed under the MIT License.

