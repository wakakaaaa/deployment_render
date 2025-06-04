
from app.config import get_settings
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.crud import fetch_data
from app.schemas import TableResponse, Row

import pandas as pd
import os

app = FastAPI()

# DEFAULT_QUERY = '''
#     select
# 	to_date(forecastmonth,'YYYY-MM-DD') AS forecastmonth
#    ,market
#    ,region
#    ,ordermonth
#    ,sum(itemqty*cbm )                   sales_cbm
# from
# 	dwd_prod.public.hist_item_rolling_forecast_version rirf
# where
# 	monthdiff     >=1
# and version       ='FINAL'
# and forecastmonth ='2025-04-01'
# 	--					= (select max(forecastmonth)  from hist_item_rolling_forecast_version)
# group by
# 	forecastmonth
#    ,market
#    ,region
#    ,ordermonth
#
# union
# -- manually add current month(forecast month)actual sales to forecast
# select
# 	'2025-04-01'                         forecastmonth
#    ,market
#    ,region
#    ,date_trunc('month', fd.so_create_dt) ordermonth
#    ,sum(fd.total_cbm )                   sales_cbm
# from
# 	dwd_prod.public.fact_deliveryorder fd
# where
# 	fd.orig_location in('MY-Stock'
# 					   ,'ACR-Stock'
# 					   ,'MY-Perth-Transit'
# 					   ,'VIC1-Stock'
# 					   ,'CA1-Stock'
# 					   ,'CA2-Stock'
# 					   ,'NJ1-Stock'
# 					   ,'NJ2-Stock'
# 					   ,'IL1-Stock'
# 					   ,'TX1-Stock'
# 					   ,'WA1-Stock'
# 					   ,'WA2-Stock'
# 					   ,'GA1-Stock')
# and fd.sp_state not in ('Cancelled'
# 					   ,'cancel'
# 					   ,'CANCELLED'
# 					   ,'INVALID'
# 					   ,'Rejected')
# and fd.direction ='Delivery'
# and date_trunc('month', fd.so_create_dt) between date_trunc('month',add_months(current_date,-5)) and date_trunc('month',add_months(current_date,-1))
# group by
# 	date_trunc('month', fd.so_create_dt)
#    ,market
#    ,region
# '''

NEW_QUERY = '''
    SELECT
        *
    FROM
        railway.outbound_forecast
'''
@app.get("/data", response_model=TableResponse)
def get_data(db: Session = Depends(get_db)):
    try:
        result = fetch_data(db, NEW_QUERY)
        if not result:
            return {"columns": [], "rows": []}

        columns = result[0].keys()
        rows = [Row(data=list(row)) for row in result]
        return {"columns": list(columns), "rows": rows}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# uvicorn app.main:app --host 0.0.0.0 --port 10000

def test_fetch():
    db = next(get_db())  # 手动调用生成器，获取连接
    try:
        result = fetch_data(db, NEW_QUERY)
        df = pd.DataFrame(result)
        print(df)
    finally:
        db.close()

@app.on_event("startup")
async def startup_event():
    settings = get_settings()
    print("✅ Environment variables loaded:")
    print("MYSQL_USER:", settings.MYSQL_USER)
    print("MYSQL_HOST:", settings.MYSQL_HOST)
    print("MYSQL_PORT:", settings.MYSQL_PORT)
    print("MYSQL_DB:", settings.MYSQL_DB)


if __name__ == "__main__":
    # print("REDSHIFT_USER =", settings.REDSHIFT_USER)
    test_fetch()