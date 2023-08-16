-- 루시와 엘라 찾기
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
    FROM ANIMAL_INS 
    WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
    ORDER BY ANIMAL_ID;

-- 상품 별 오프라인 매출 구하기
SELECT PRODUCT_CODE
        , SUM(SALES) AS SALES
    FROM (
          SELECT P.PRODUCT_CODE
                , P.PRICE
                , OFF.SALES_AMOUNT
                , P.PRICE*OFF.SALES_AMOUNT AS SALES
            FROM OFFLINE_SALE AS OFF
            LEFT JOIN PRODUCT AS P
            ON OFF.PRODUCT_ID = P.PRODUCT_ID
         )AS A
    GROUP BY P.PRODUCT_CODE
    ORDER BY SALES desc, P.PRODUCT_CODE asc;