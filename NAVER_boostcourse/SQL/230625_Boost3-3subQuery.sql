/* 
    서브 쿼리 : select문 안에 또 다른 select문이 있는 명령어 
    _ select 절
    _ from 절
    _ where 절
*/

-- use practice;

/* JOIN 대신 서브쿼리로 결합 */
select *
        , (select GENDER from CUSTOMER where A.MEM_NO = MEM_NO) as GENDER
        from SALES as A;

/* 1000970 회원 정보 확인 */
select *
    from CUSTOMER
    where MEM_NO = '1000970';


/* 
    FROM 절 서브쿼리
    from (테이블 형태)
*/
select *
    from (
        select MEM_NO, count(ORDER_NO) as 주문횟수  -- as 주문횟수 : 열 이름 지정 필요
        from SALES
        group by MEM_NO                           -- group by 가능
        )as A;                                    -- 새로운 테이블 이름 지정 필요


/* where 절 서브쿼리 */
-- 2019년 주문횟수
select count(ORDER_NO) as 주문횟수
    from SALES
    where MEM_NO in (select MEM_NO from CUSTOMER where YEAR(JOIN_DATE) = 2019);

-- YEAR : 날짜형 함수 >> 다음 챕터
select *, YEAR(JOIN_DATE)
    from CUSTOMER;

/**/
select MEM_NO from CUSTOMER where year(JOIN_DATE) = 2019;
-- = 리스트 ('1000001', '1000002', ...)

select count(A.ORDER_NO) as 주문횟수
    from SALES as A 
    inner join CUSTOMER as B 
    on A.MEM_NO = B.MEM_NO
    where year(B.JOIN_DATE) = 2019;

/*  정리
    select _ '열' (스칼라)
           _ JOIN보다 처리 늦음
    from   _ '테이블' (열 이름 및 테이블명 지정)
           _ 최다 사용, JOIN과 함께
    where  _ '리스트'
*/
/* 최다 사용 from 절 형태
    (
        from + join
        where
        group by
        having
        select
        order by
    )
*/
create temporary table SALES_SUB_QUERY
select A.구매횟수, -- A와 B에 모두 MEM_NO열이 있기 때문에 중복되면 안됨
        B.*
    from (
            select MEM_NO, count(ORDER_NO) as 구매횟수
            from SALES
            group by MEM_NO
        )as A 
    inner join CUSTOMER as B 
    on A.MEM_NO = B.MEM_NO;

-- 조회
select * from SALES_SUB_QUERY;

-- 원하는 열이 합쳐진 테이블(SALES_SUB_QUERY) 에서 원하는 조건 검색 가능
select *
    from SALES_SUB_QUERY
    where GENDER = 'MAN';

select ADDR, sum(구매횟수) as 구매횟수
    from SALES_SUB_QUERY
    where GENDER = 'MAN'

    group by ADDR
    having sum(구매횟수) < 100
    
    order by sum(구매횟수) asc;
