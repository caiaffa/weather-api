from pydantic import BaseModel, Field


class CityBase(BaseModel):
    name: str = Field(None, title="The name of the city", min_length=3)
    state_code: str = Field(None, title="The state code of the city", min_length=2, max_length=2)
    country_code: str = Field(None, title="The country code of the city", min_length=2)
