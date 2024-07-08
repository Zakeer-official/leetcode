select round((sum(case when order_date = customer_pref_delivery_date 
and order_date = any (select min(order_date) 
from Delivery b where a.customer_id = b.customer_id) 
then 1 else 0 end) / ( select count(distinct customer_id) 
from Delivery))*100,2) immediate_percentage 
from Delivery a;