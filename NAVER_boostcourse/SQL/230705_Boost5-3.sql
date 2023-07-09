/* 재구매자 및 구매주기 분석 */
USE NaverBoost;

/*  정의부터
	구매간격 = (최근 - 최초)
    구매주기 = (최근 - 최초) / (구매횟수 - 1)
*/
SELECT * FROM CUSTOMER; -- A
SELECT * FROM SALES;    -- B
SELECT * FROM PRODUCT;  -- C

/*SELECT *
		, D.구매횟수
	FROM (
			SELECT mem_no
				    , COUNT(mem_no) AS 구매횟수
                    , min(
                FROM SALES
                GROUP BY mem_no
    )AS D
    GROUP BY mem_no;*/

-- TEST --

/*
SELECT mem_no
		, datediff(MIN(order_date), MAX(order_date)) AS 테스트
	FROM SALES
    GROUP BY mem_no;       
-- 결과 : 마이너스 나옴
*/
    
SELECT *
		-- ,COUNT(order_no) AS 구매횟수
	FROM (
		SELECT mem_no
				, MIN(order_date) AS 최초구매
                , MAX(order_date) AS 최근구매
                , COUNT(order_no) AS 구매횟수
                , IF(COUNT(order_no)>1 and datediff(MAX(order_date), MIN(order_date))>=1 ,0,1) AS 재구매
                , datediff(MAX(order_date), MIN(order_date)) AS 구매간격
				, datediff(MAX(order_date), MIN(order_date))/(COUNT(order_no)-1) AS 구매주기  -- 구매주기 소수점 있음
	 	FROM SALES
        GROUP BY mem_no
	) AS NW;

