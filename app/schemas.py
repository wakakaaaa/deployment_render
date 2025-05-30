from pydantic import BaseModel
from typing import List, Any

class Row(BaseModel):
    data: List[Any]

class TableResponse(BaseModel):
    columns: List[str]
    rows: List[Row]