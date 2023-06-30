/* 
    데이터 마트 : 분석에 필요한 데이터를 가공한 분석용 데이터
    _ 요약 변수 : 종합
    _ 파생 변수 : 특정 조건이나 함수로 의미부여
*/

use PRACTICE;

/* 회원 구매 정보 */

create temporary table CUSTOMER_PUR_INFO as -- 임시테이블로 저장
select A.MEM_NO, A.GENDER, A.BIRTHDAY, A.ADDR, A.JOIN_DATE
    , SUM(B.SALES_QTY * C.PRICE) as 구매금액
    , count(B.ORDER_NO)          as 구매횟수
    , SUM(B.SALES_QTY)           as 구매수량
from CUSTOMER as A 
left join SALES as B 
on A.MEM_NO = B.MEM_NO
left join product as C 
on B.PRODUCT_CODE = C.PRODUCT_CODE
group by A.MEM_NO, A.GENDER, A.BIRTHDAY, A.ADDR, A.JOIN_DATE;

/* 확인 */
-- select * from CUSTOMER_PUR_INFO;

/* 회원 연령대 확인 */
select *  
    -- case when 순서 주의, < 50 먼저 쓰면 그 후 <10 는 뛰어넘음
    case when 나이 < 10 then '10대 미만'
         when 나이 < 20 then '10대'
         --when 나이 < 20 then '10대'
         --when 나이 < 20 then '10대'
         else '50대 이상' end as 연령대
    from (
            select *
                    , 2021 - YEAR(BIRTHDAY) +1 as 나이
                from CUSTOMER
        )as A;

/* 회원 구매정보 + 연령대 임시테이블 */
create temporary table CUSTOMER_PUR_INFO_AGEBAND as
    select A.*
        , B.연령대
    from CUSTOMER_PUR_INFO as A 
    left join CUSTOMER_AGEBAND as B 
    on A.MEM_NO = B.MEM_NO;
    


