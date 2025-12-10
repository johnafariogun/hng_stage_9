from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PAYSTACK_SECRET_KEY: str = "sk_test_xxxxxxxxxxxxxxxxxxxxx"
    PAYSTACK_BASE_URL: str = "https://api.paystack.co"
    PAYSTACK_PUBLIC_KEY: str = "pk_test_xxxxxxxxxxxxxxxxxxxxx"


settings = Settings()