from datetime import timedelta

EXPIRY_MAP = {
    "burn": {"max_views": 1},
    "1_hour": {"delta": timedelta(hours=1)},
    "1_day": {"delta": timedelta(days=1)},
    "1_week": {"delta": timedelta(weeks=1)},
    "2_weeks": {"delta": timedelta(weeks=2)},
    "1_month": {"delta": timedelta(days=30)},
    "6_months": {"delta": timedelta(days=180)},
    "1_year": {"delta": timedelta(days=365)},
    "never": {},
}
