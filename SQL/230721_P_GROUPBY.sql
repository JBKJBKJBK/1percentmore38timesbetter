-- 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기
SELECT /*OPTIONS,*/ CAR_TYPE, COUNT(CAR_ID) AS CARS
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE OPTIONS LIKE "%열선시트%" OR
          OPTIONS LIKE "%통풍시트%" OR 
          OPTIONS LIKE "%가죽시트%" 
    GROUP BY CAR_TYPE
    ORDER BY CAR_TYPE;

-- 저자 별 카테고리 별 매출액 집계하기
SELECT X.AUTHOR_ID, X.AUTHOR_NAME, X.CATEGORY, SUM(X.TOTAL_SALES)-- , X.SALES_DATE
    FROM (
        SELECT A.*, B.SALES, C.author_name
                , (A.PRICE * B.SALES) AS TOTAL_SALES
                , date_format(B.SALES_DATE, '%Y-%m') AS SALES_DATE
            FROM BOOK AS A
            -- WHERE SALES_DATE == '2022-01'
            INNER
            JOIN BOOK_SALES AS B
            ON A.BOOK_ID = B.BOOK_ID
            INNER
            JOIN AUTHOR AS C
            ON A.author_id = C.author_id
        ) AS X
    WHERE X.SALES_DATE = '2022-01'
    GROUP BY X.AUTHOR_ID, X.CATEGORY
    ORDER BY X.AUTHOR_ID, X.CATEGORY desc;