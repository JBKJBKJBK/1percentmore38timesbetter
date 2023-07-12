USE NaverBoost;

CREATE TABLE PRODUCT_GROUTH AS
SELECT A.MEM_NO
		, B.CATEGORY
        , B.BRAND
        , A.SALES_QTY * B.PRICE AS 구매금액
        , CASE WHEN DATE_FORMAT(ORDER_DATE, '%Y-%m') BETWEEN '2020-01' AND '2020-03' THEN '2020 1분기'
               WHEN DATE_FORMAT(ORDER_DATE, '%Y-%m') BETWEEN '2020-04' AND '2020-06' THEN '2020 2분기'
			   END AS 분기
	FROM SALES AS A
    LEFT JOIN PRODUCT AS B
    ON A.PRODUCT_CODE = B.PRODUCT_CODE
    WHERE DATE_FORMAT(ORDER_DATE, '%Y-%m') BETWEEN '2020-01' AND '2020-06';

SELECT *
		-- CASE WHEN 분기 = '2020 1분기' THEN 
	FROM PRODUCT_GROUTH;

SELECT CATEGORY
			/*
			, SUM(구매금액) AS TEST
            , SUM(IF(분기='2020 1분기','구매금액', '')) AS 2020_1분기_구매금액
            , SUM(IF(분기='2020 2분기','구매금액', '')) AS 2020_2분기_구매금액
            */
            /* 이거 안됨...! 
			, SUM(CASE WHEN 분기 = '2020 2분기' THEN '구매금액' END) AS 2020_2분기_구매금액
            >>> '구매금액'이 아니라 구매금액 */ 
            , SUM(CASE WHEN 분기 = '2020 1분기' THEN 구매금액 END) AS 2020_1분기_구매금액
            , SUM(CASE WHEN 분기 = '2020 2분기' THEN 구매금액 END) AS 2020_2분기_구매금액
		FROM PRODUCT_GROUTH
		GROUP BY CATEGORY;
        -- ORDER BY  

-- 카테고리별 구매금액 성장률
SELECT *
		, (2020_2분기_구매금액 - 2020_1분기_구매금액) / 2020_1분기_구매금액 AS 성장률
	FROM (
			SELECT CATEGORY
				, SUM(CASE WHEN 분기 = '2020 1분기' THEN 구매금액 END) AS 2020_1분기_구매금액
				, SUM(CASE WHEN 분기 = '2020 2분기' THEN 구매금액 END) AS 2020_2분기_구매금액
			FROM PRODUCT_GROUTH
            GROUP BY CATEGORY
		) AS A;

-- beauty 카테고리 브랜드 구매지표
SELECT * FROM SALES;
SELECT * FROM PRODUCT;

CREATE TABLE BEAUTY_CATE AS
SELECT BRAND
		, 구매금액
	FROM PRODUCT_GROUTH
    WHERE CATEGORY = "beauty";

CREATE TABLE BEAUTY_CATE_PERCENT AS
SELECT BRAND
		, SUM(A.구매금액) AS 브랜드_구매금액
        , SUM(A.구매금액) / (SELECT SUM(B.구매금액) FROM BEAUTY_CATE AS B) AS 브랜드_매출비율
	   FROM BEAUTY_CATE AS A
       GROUP BY BRAND
       ORDER BY 브랜드_매출비율 desc;
       
-- 합계 확인 = 1
SELECT SUM(브랜드_매출비율) FROM BEAUTY_CATE_PERCENT;

/* 부스트코스 답안 */
SELECT BRAND
		, COUNT(DISTINCT MEM_NO) AS 구매횟수
        , SUM(구매금액) AS 구매금액_합계
        , SUM(구매금액) / COUNT(DISTINCT MEM_NO) AS 인당_구매금액
	FROM PRODUCT_GROUTH
    WHERE CATEGORY = 'beauty'
    GROUP BY BRAND
    ORDER BY 4 desc;