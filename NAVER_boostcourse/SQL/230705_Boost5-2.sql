/*. 고객 가치 평가 모형
	Recency		최근
    Frequency	구매빈도
    Monetary	구매금액
*/

-- CUSTOMER TABLE + 구매금액, 횟수, 주문일자:2020
/*  분석보고서
	RFM 세분화별 회원수
			   매출액
               인당 구매금액
*/

SELECT * FROM customer;
SELECT * FROM sales;
SELECT * FROM product;

USE NaverBoost;

-- CREATE TABLE TEMP AS
-- SELECT B.mem_no
-- 		, sum(B.sales_qty * C.price) AS 구매금액  -- M
-- 		, count(B.order_no) AS 구매횟수 -- F 
-- 	FROM sales AS B
-- 	LEFT 
-- 	JOIN product AS C 
-- 	on B.product_code = C.product_code
-- 	WHERE YEAR(B.order_date) = '2020' -- R 
-- 	GROUP BY B.mem_no;
--     
-- SELECT * FROM TEMP;
-- 원하는 방향대로 출력됨

DROP TABLE RFM;

CREATE TABLE RFM AS
SELECT A.*
		, D.구매금액
        , D.구매횟수
	FROM customer AS A
    LEFT 
    JOIN TEMP AS D
	ON A.mem_no = D.mem_no;
    
SELECT * FROM RFM;
-- 구매금액과 횟수 NULL

-- 강의코드
-- CREATE TABLE CLASSEX AS
-- SELECT A.*
-- 		, B.구매금액
--         , B.구매횟수
-- 	FROM customer AS A 
--     LEFT
--     JOIN (
-- 			SELECT A.mem_no
-- 				    , sum(A.sales_qty * B.price) AS 구매금액  -- M
--                     , count(A.order_no) AS 구매횟수 -- F 
-- 				FROM sales AS A
--                 LEFT 
--                 JOIN product AS B
--                 on A.product_code = B.product_code
--                 WHERE YEAR(A.order_date) = '2020' -- R 
--                 GROUP BY A.mem_no
-- 			)AS B
-- 	ON A.mem_no = B.mem_no;
--     
-- SELECT * FROM CLASSEX;
-- -- 이것도 NULL...
-- 구매 이력이 없는 회원!
-- DROP TABLE CLASSEX;
-- DROP TABLE TEMP;

/* VIP */
SELECT *
		, CASE WHEN 구매금액 > 5000000 THEN 'VIP'
          	   WHEN 구매금액 > 1000000 OR 구매횟수 > 3 THEN '우수회원'
               WHEN 구매금액 > 0 THEN '일반회원'
			   ELSE '잠재회원' END AS 회원등급
	FROM RFM;

SELECT 회원등급
		, count(mem_no) AS 회원수
	FROM (
		SELECT *
			, CASE WHEN 구매금액 > 5000000 THEN "VIP"
				   WHEN 구매금액 > 1000000 OR 구매횟수 > 3 THEN "우수회원"
				   WHEN 구매금액 > 0 THEN "일반회원"
				   ELSE '잠재회원' END AS 회원등급
			FROM RFM
		) AS A -- AS A 없으니 에러남
	GROUP BY 회원등급;


SELECT 회원등급
		, count(mem_no) AS 회원수
		, sum(구매금액) AS 구매금액
        , sum(구매금액) / count(mem_no) AS 인당구매금액
	FROM (
		SELECT *
			, CASE WHEN 구매금액 > 5000000 THEN "VIP"
				   WHEN 구매금액 > 1000000 OR 구매횟수 > 3 THEN "우수회원"
				   WHEN 구매금액 > 0 THEN "일반회원"
				   ELSE '잠재회원' END AS 회원등급
			FROM RFM
		) AS A -- AS A 없으니 에러남
	GROUP BY 회원등급; 
