create database NaverBoost;

use NaverBoost;

-- select * from CUSTOMER;   
DROP TABLE customer_profile;

CREATE TABLE CUSTOMER_PROFILE AS 
SELECT A.*
		, DATE_FORMAT(JOIN_DATE, '%y-%m') AS 가입년월
        , 2021 - YEAR(birthday) + 1 as 나이
        , CASE WHEN 2021 - YEAR(birthday) + 1 < 20 THEN '10대 이하'
 			   WHEN 2021 - YEAR(birthday) + 1 < 30 THEN '20대'
 			   WHEN 2021 - YEAR(birthday) + 1 < 40 THEN '30대'
 			   WHEN 2021 - YEAR(birthday) + 1 < 50 THEN '40대'
               ELSE '50대 이상' END AS 연령대
 		, CASE WHEN B.MEM_NO is not null THEN '구매'
 			   ELSE '미구매' END AS 구매여부
	FROM CUSTOMER as A
    LEFT JOIN (SELECT DISTINCT MEM_NO FROM SALES) AS B
    ON A.MEM_NO = B.MEM_NO;

SELECT * FROM CUSTOMER;
SELECT * FROM SALES;
SELECT * FROM CUSTOMER_PROFILE; 

/* 1. 가입년월별 회원수 */
SELECT 가입년월
		, COUNT(MEM_NO) AS 회원수
	FROM CUSTOMER_PROFILE
    GROUP BY 가입년월;
    
    
/* 2. 성별 평균 연령, 성별 및 연령대별 회원수 */
SELECT gender
		, 연령대
		, count(mem_no) AS 회원수
	FROM customer_profile
    GROUP BY gender, 연령대
    ORDER BY gender, 연령대;

/* 3. 2. + 구매여부 */
SELECT gender
		, 연령대
        , COUNT(mem_no) AS 회원수
        , 구매여부
	FROM customer_profile
    GROUP BY gender, 연령대, 구매여부	ORDER BY gender, 연령대, 구매여부;