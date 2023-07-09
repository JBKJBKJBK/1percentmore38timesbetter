/* 재구매자 및 구매주기 분석 */
USE NaverBoost;

/*
	구매간격 = (최근 - 최초) / (구매횟수 - 1)
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

-- TEST 
SELECT *
		, count(mem_no) AS 구매횟수
	FROM SALES
    GROUP BY mem_no;  
