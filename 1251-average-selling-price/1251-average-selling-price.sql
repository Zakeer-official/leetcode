SELECT
    p.product_id,
    COALESCE(ROUND(SUM(p.price * coalesce(u.units, 0)) / NULLIF(SUM(u.units), 0), 2), 0) AS average_price
FROM
    Prices p left join UnitsSold u
     on p.product_id = u.product_id
              AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY
    p.product_id;
