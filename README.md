# Hangar — Django E-Commerce Platform

A Django-based e-commerce application with product catalog, category browsing, search, order tracking, and user profiles. Currently in active refactor toward a production-grade, portfolio-ready state.

> **Status:** 🚧 Under active development. See [Known Issues & Roadmap](#known-issues--roadmap) — this project is intentionally being rebuilt in public, one reviewable feature branch at a time.

## Features

- Product catalog with category-based browsing
- Product search
- Shopping cart and checkout flow
- Order tracking by order ID + email
- Contact form
- User registration, login/logout, and editable profiles (with avatar upload)
- Django admin for product/order management

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0 |
| Database | SQLite (dev) — PostgreSQL planned for production |
| Forms | django-crispy-forms |
| Images | Pillow |
| Config | python-decouple (environment variables) |

## Project Structure

```
Hangar/                 # Project config: settings, root urls, wsgi/asgi
├── settings.py
├── urls.py
└── templates/

shop/                   # Product catalog, cart, checkout, orders
├── models.py           # Product, Contact, Orders, OrderUpdate
├── views.py
├── urls.py
└── templates/shop/

authy/                  # Authentication and user profiles
├── models.py           # Profile (extends User via OneToOneField)
├── forms.py
├── views.py
└── templates/
```

## Getting Started

### Prerequisites

- Python 3.12+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/<you>/hangar-ecommerce.git
cd hangar-ecommerce

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

This project uses `python-decouple` to keep secrets out of source control. Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Generate a secret key with:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Run migrations and start the server

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`. Admin panel at `/admin/`.

## Known Issues & Roadmap

This project is being refactored feature-by-feature with full commit history. Tracked here so the history is honest rather than hidden:

- [ ] Fix: search crashes with a `TypeError` on any query (`fix/search-crash`)
- [ ] Redesign `Orders` to use a proper `OrderItem` through-model instead of a raw JSON string field
- [ ] Switch `Product.price` from `IntegerField` to `DecimalField`
- [ ] Harden production security settings (currently commented out in `settings.py`)
- [ ] Add automated test coverage (currently none)
- [ ] Dockerize + CI/CD pipeline

## Contributing

This is currently a solo learning/portfolio project. Feature work happens on branches named `feature/<name>` or `fix/<name>` and merges to `main` via reviewed, scoped commits.

## License

MIT