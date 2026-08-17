-- dbt Staging Model: stg_orders.sql
-- Session 10 - In-Lake Transformation with dbt

with source_data as (
    select
        cast(id as string) as order_id,
        cast(user_id as string) as customer_id,
        cast(order_date as date) as order_date,
        cast(status as string) as order_status,
        cast(amount as decimal(18,2)) as total_amount
    from {{ source('raw', 'orders') }}
)

select *
from source_data