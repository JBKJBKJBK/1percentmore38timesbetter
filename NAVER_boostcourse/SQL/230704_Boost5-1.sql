create database NaverBoost;

use NaverBoost;

-- select * from CUSTOMER;   

CREATE TABLE CUSTOMER_PROFILE AS
SELECT A.*
		, DATE_FORMAT(JOIN_DATE, '%y-%m') AS 가입년월
        , 2021 - YEAR(birthday) + 1 as 나이
        , CASE WHEN 2021 - YEAR(birthday) + 1 < 20 THEN '10대 이하'
 			   WHEN 2021 - YEAR(birthday) + 1 < 30 THEN '20대'
               ELSE '30대 이상' END AS 연령대
 		, CASE WHEN B.MEM_NO is not null THEN '구매'
 			   ELSE '미구매' END AS 구매여부
	FROM CUSTOMER as A
    LEFT JOIN (SELECT DISTINCT MEM_NO FROM SALES) AS B
    ON A.MEM_NO = B.MEM_NO;

SELECT * FROM CUSTOMER;
SELECT * FROM SALES;
SELECT * FROM CUSTOMER_PROFILE; 





