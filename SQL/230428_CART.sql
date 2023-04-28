"""
select CART_ID, group_concat(NAME) as NAME 
from CART_PRODUCTS
group by CART_ID
"""

select CART_ID
from (select CART_ID, group_concat(NAME) as NAME 
from CART_PRODUCTS
group by CART_ID) newTable    
---- 서브쿼리 뒤에 이름 붙여줘야 함
---- Every derived table must have its own alias
where NAME Like '%Milk%' and NAME Like '%Yogurt%'
---- NAME LIKE '%Milk%' and '%Yogurt%'
---- 라고하면 아무것도 안 나옴