# Test Data Guide

Comprehensive guide for working with test data in the PMS Test Automation Framework.

## Table of Contents

- [Overview](#overview)
- [Data Sources](#data-sources)
- [Using Static Data](#using-static-data)
- [Dynamic Data Generation](#dynamic-data-generation)
- [Data Factories](#data-factories)
- [Best Practices](#best-practices)

---

## Overview

This framework provides multiple approaches for test data management:

1. **Static Data Files** - JSON/CSV files with predefined test data
2. **Dynamic Generation** - Faker-based random data generation
3. **Data Factories** - Flexible data creation with customization
4. **Builder Pattern** - Complex scenario construction

---

## Data Sources

### Directory Structure

```
src/tests/data/
├── guests/
│   ├── guest_data.json          # Guest test data
│   └── bulk_guests.csv          # Bulk guest data
├── reservations/
│   └── reservation_data.json    # Reservation test data
├── rooms/
│   └── room_data.json           # Room configuration data
└── settings/
    └── test_config.json         # Test configuration
```

---

## Using Static Data

### JSON Data Files

#### Guest Data (`guests/guest_data.json`)

```json
{
  "valid_guest": {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "+1-555-0100"
  },
  "vip_guest": {
    "name": "Jane Smith",
    "vip_status": "platinum",
    "loyalty_number": "PLAT-123456"
  }
}
```

#### Using in Tests

```python
import pytest

def test_create_guest(valid_guest):
    """Test using static guest data."""
    assert valid_guest["email"] is not None
    browser.guest.create(valid_guest)
```

### CSV Data Files

#### Bulk Guests (`guests/bulk_guests.csv`)

```csv
guest_name,email,phone,room_type
John Doe,john@email.com,+1-555-0101,DELUXE
Jane Smith,jane@email.com,+1-555-0102,SUITE
```

#### Using in Tests

```python
@pytest.fixture
def bulk_guests():
    """Load bulk guests from CSV."""
    return load_csv_data("guests/bulk_guests.csv")

def test_bulk_reservations(bulk_guests):
    """Test creating multiple reservations."""
    for guest in bulk_guests:
        create_reservation(guest)
```

---

## Dynamic Data Generation

### Using Faker

The framework integrates [Faker](https://faker.readthedocs.io/) for random data:

```python
from faker import Faker

fake = Faker()

# Generate random data
guest = {
    "name": fake.name(),
    "email": fake.email(),
    "phone": fake.phone_number(),
    "address": fake.street_address(),
    "city": fake.city(),
    "country": fake.country()
}
```

### Pre-built Fixtures

```python
@pytest.fixture
def random_guest():
    """Generate random guest data."""
    return {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number()
    }

def test_with_random_data(random_guest):
    """Test with randomly generated guest."""
    create_guest(random_guest)
```

### Data Generators

#### Guest Generator

```python
from tests.fixtures import GuestDataGenerator

# Create basic guest
guest = GuestDataGenerator.create_guest()

# Create VIP guest
vip = GuestDataGenerator.create_vip_guest()

# Create corporate guest
corp = GuestDataGenerator.create_corporate_guest("Tech Corp")

# Create bulk guests
guests = GuestDataGenerator.create_bulk_guests(100)
```

#### Reservation Generator

```python
from tests.fixtures import ReservationDataGenerator

# Create basic reservation
reservation = ReservationDataGenerator.create_reservation()

# Create weekend reservation
weekend = ReservationDataGenerator.create_weekend_reservation()

# Create group reservation
group = ReservationDataGenerator.create_group_reservation(
    group_name="Conference 2026",
    num_rooms=50
)
```

#### Room Generator

```python
from tests.fixtures import RoomDataGenerator

# Create single room
room = RoomDataGenerator.create_room(
    number="301",
    room_type="DELUXE"
)

# Create room inventory
inventory = RoomDataGenerator.create_room_inventory(
    floor_count=5,
    rooms_per_floor=10
)  # Creates 50 rooms
```

---

## Data Factories

### Guest Factory

```python
@pytest.fixture
def guest_factory():
    """Factory for creating guest data."""
    def _create_guest(name=None, email=None, **kwargs):
        return {
            "name": name or fake.name(),
            "email": email or fake.email(),
            "phone": fake.phone_number(),
            **kwargs
        }
    return _create_guest

# Usage
def test_with_factory(guest_factory):
    # Create default guest
    guest1 = guest_factory()

    # Create custom guest
    guest2 = guest_factory(
        name="Custom User",
        email="custom@example.com",
        country="Canada"
    )
```

### Reservation Factory

```python
@pytest.fixture
def reservation_factory():
    """Factory for creating reservation data."""
    def _create_reservation(guest_name=None, **kwargs):
        arrival = fake.date_between('today', '+30d')
        return {
            "guest_name": guest_name or fake.name(),
            "arrival_date": arrival.isoformat(),
            "departure_date": fake.date_between(arrival, '+60d').isoformat(),
            **kwargs
        }
    return _create_reservation

# Usage
def test_custom_reservation(reservation_factory):
    reservation = reservation_factory(
        room_type="SUITE",
        adults=2,
        children=1
    )
```

---

## Builder Pattern

For complex test scenarios:

```python
from tests.fixtures import create_test_scenario

def test_complete_booking():
    """Test complete booking scenario."""
    scenario = (
        create_test_scenario()
        .with_vip_guest()
        .with_reservation(room_type="SUITE")
        .with_room(status="VA")
        .with_payment(499.00)
        .build()
    )

    # Use scenario data
    create_guest(scenario["guest"])
    create_reservation(scenario["reservation"])
    assign_room(scenario["room"])
    process_payment(scenario["payments"][0])
```

---

## Parametrized Testing

### Single Parameter

```python
@pytest.mark.parametrize("guest_type", [
    "valid_guest",
    "vip_guest",
    "corporate_guest"
])
def test_guest_types(guest_type, guest_data):
    """Test with multiple guest types."""
    guest = guest_data[guest_type]
    assert guest["name"] is not None
```

### Multiple Parameters

```python
@pytest.mark.parametrize("adults,children,valid", [
    (1, 0, True),   # 1 adult - valid
    (2, 2, True),   # Family - valid
    (0, 0, False),  # No guests - invalid
    (5, 0, False),  # Too many - invalid
])
def test_guest_count(adults, children, valid):
    """Test guest count validation."""
    is_valid = validate_guest_count(adults, children)
    assert is_valid == valid
```

### From CSV File

```python
@pytest.mark.parametrize("guest_data", load_csv_data("guests/bulk_guests.csv"))
def test_from_csv(guest_data):
    """Test with data from CSV."""
    create_reservation(guest_data)
```

---

## Data Cleanup

### Using Fixtures

```python
@pytest.fixture
def test_guest(browser):
    """Create and cleanup test guest."""
    # Setup
    guest_id = browser.guest.create(test_data)

    yield guest_id

    # Teardown
    browser.guest.delete(guest_id)

def test_with_cleanup(test_guest):
    """Test with automatic cleanup."""
    # Test code here
    pass
```

### Tracking Pattern

```python
@pytest.fixture
def cleanup_tracker():
    """Track created resources."""
    resources = {"guests": [], "reservations": []}
    yield resources

    # Cleanup all tracked resources
    for guest_id in resources["guests"]:
        delete_guest(guest_id)
```

---

## Best Practices

### 1. Use Appropriate Data Source

- **Static Data**: For specific test scenarios
- **Random Data**: For general testing
- **Factories**: When you need customization
- **Builders**: For complex scenarios

### 2. Keep Tests Independent

```python
# Good: Each test creates its own data
def test_create_guest():
    guest = create_test_guest()
    assert guest is not None

# Avoid: Tests depend on shared data
def test_create_guest():
    # Uses global data
    assert global_guest is not None
```

### 3. Use Meaningful Names

```python
# Good
vip_guest_with_high_points = create_vip_guest(points=10000)

# Avoid
g1 = create_guest()
```

### 4. Validate Data

```python
def test_reservation_dates():
    reservation = create_reservation()

    # Validate date logic
    arrival = parse_date(reservation["arrival_date"])
    departure = parse_date(reservation["departure_date"])
    assert departure > arrival, "Departure must be after arrival"
```

### 5. Clean Up Data

```python
@pytest.fixture
def test_data():
    # Setup
    data = create_test_data()
    yield data

    # Cleanup
    delete_test_data(data)
```

---

## Examples

See `src/tests/examples/test_data_examples.py` for comprehensive examples.

---

## Troubleshooting

### Issue: Data file not found

**Solution:**
```bash
# Verify file path
ls src/tests/data/guests/guest_data.json

# Check DATA_DIR in fixtures
from pathlib import Path
DATA_DIR = Path(__file__).parent / "data"
```

### Issue: Faker not generating unique data

**Solution:**
```python
# Use Faker with seed for reproducibility
from faker import Faker
fake = Faker()
fake.seed_instance(12345)

# Or create new instance
fake = Faker()
```

### Issue: CSV data not loading correctly

**Solution:**
```python
# Check CSV format
with open('data.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Verify headers match expected fields
print(reader.fieldnames)
```

---

## Additional Resources

- [Faker Documentation](https://faker.readthedocs.io/)
- [pytest Fixtures](https://docs.pytest.org/en/stable/fixture.html)
- [Parametrized Tests](https://docs.pytest.org/en/stable/how-to/parametrize.html)

---

*Last updated: March 11, 2026*
