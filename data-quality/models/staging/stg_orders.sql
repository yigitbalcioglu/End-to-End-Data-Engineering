-- Example staging model selecting from the destination Postgres loaded by ELT.
select
    id,
    user_id,
    product_id,
    status,
    amount,
    created_at
from {{ source('public', 'orders') }}
