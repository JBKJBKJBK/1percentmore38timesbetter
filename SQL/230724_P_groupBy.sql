-- 즐겨찾기가 가장 많은 식당 정보 출력하기 (미통과)
SELECT FOOD_TYPE, REST_ID, REST_NAME, MAX(FAVORITES) AS FAVORITES
    FROM REST_INFO
    GROUP BY FOOD_TYPE
    ORDER BY FAVORITES desc;

-- 조건에 맞는 사용자와 총 거래금액 조회하기
SELECT USER_ID, NICKNAME, SUM(PRICE) AS TOTAL_SALES
    FROM (
        SELECT A.USER_ID, A.NICKNAME, B.PRICE, B.STATUS
            FROM USED_GOODS_USER AS A
            INNER JOIN USED_GOODS_BOARD AS B
            ON A.USER_ID = B.WRITER_ID
            WHERE B.STATUS = 'DONE'
    ) AS C    --  AS C 없으면 에러
    GROUP BY USER_ID
    HAVING TOTAL_SALES >= 700000
    ORDER BY TOTAL_SALES;

-- 카테고리 별 도서 판매량 집계하기 (아직 통과 못함)
SELECT A.CATEGORY
        , SUM(B.SALES) AS TOTAL_SALES
    FROM BOOK AS A
    INNER JOIN BOOK_SALES AS B
    ON A.BOOK_ID = B.BOOK_ID
    -- WHERE date_format(B.SALES_DATE, '%Y-%m') = '2022-01'
    -- GROUP BY A.CATEGORY
    -- HAVING date_format(B.SALES_DATE, '%Y-%m') = '2022-01'    # 에러 >> where로
    -- ORDER BY TOTAL_SALES;