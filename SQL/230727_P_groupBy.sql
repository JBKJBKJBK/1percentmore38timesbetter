-- 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기
SELECT CAR_ID
        , CASE WHEN "2022-10-16" in (START_DATE, END_DATE) THEN "대여중"
          ELSE "대여 가능" END
          AS AVAILABILITY
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    # WHERE "2022-10-16" in (START_DATE, END_DATE)
    ORDER BY CAR_ID;
-- >> 에러 : 2022-10-05 00:00:00 ~ 2022-11-14 00:00:00 일 때 결과 반대
-- group by 없음



-- 가격대 별 상품 개수 구하기
SELECT FLOOR(PRICE*0.0001)*10000 AS PRICE_GROUP
        ,COUNT(PRODUCT_ID) AS PRODUCTS
    FROM PRODUCT
    GROUP BY PRICE_GROUP
    ORDER BY PRICE_GROUP
-- >> FLOOR 자릿수?, round, ceil later