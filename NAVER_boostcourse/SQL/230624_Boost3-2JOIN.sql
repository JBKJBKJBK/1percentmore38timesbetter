/* 관계 복습 */

/*  
    * ERM (Entity-Relationship Modeling)
    개체-관계 모델링
    관계형 DB에 테이블을 모델링할 때 사용
    * 개체 (entity) : 하나 이상의 속성(Attribute)으로 구성된 객체
    * 관계 (Relationship) : 속성(Entity)으로 구성된 객체

    EX
    회원 테이블(E) + 상품 테이블(E) >> 주문 테이블(R)

    * ERD (Entity-Relationship Diagram)
    * FK (Foreign Key) : 다른 테이블에서 PK
*/

/*  INNER JOIN 
    공통값 매칭
    ex : 회원가입 + 주문이력
*/
select *
    from CUSTOMER as A  -- CUSTOMER 테이블을 A로
    inner join SALES as B --  SALES 테이블을 B로
    on A.MEM_NO = B.MEM_NO;
    -- A(CUSTOMER).열 = B(SALES).열
    -- where A.MEM_NO = '~~'
    -- where MEM_NO = '~~' -- 에러 발생

/*  LEFT(RIGHT) JOIN 
    공통값 매칭되는 데이터 결합, 
    왼쪽(오른쪽) 테이블 빈 값 NULL ex : 회원가입 + 주문이력 있는/없는
    오른쪽(왼쪽) 테이블 빈 값 탈락  ex : 회원가입/비회원 + 주문이력
*/
select *
    from CUSTOMER as A
    left join SALES as B
    on A.MEM_NO = B.MEM_NO;

select *
    from CUSTOMER as A
    right join SALES as B
    on A.MEM_NO = B.MEM_NO;
    where A.MEM_NO is null;  -- 이거 꼭 실행

-- 벤다이어그램으로 설명

/* select & join */
/*
    from + join     : 조회 & 결합
    where           : from 절 테이블을 필터링
    group by        : 열 별로 그룹화
    having          : group by 이후 테이블에서 필터링
    select          : 열 선택
    order by        : 열 정렬
*/

select * 
    from CUSTOMER as A
    inner join SALES as B
    on A.MEM_NO = B.MEM_NO;

-- 임시 테이블 생성
create temporary table CUSTOMER_SALES_INNER_JOIN
select A.* , B.ORDER_NO  -- 차이점
    from CUSTOMER as A 
    inner join SALES as BY
    on A.MEM_NO = B.MEM_NO;

-- 임시 테이블 조회
select * from CUSTOMER_SALES_INNER_JOIN

---------------------------------------
select *
    from CUSTOMER_SALES_INNER_JOIN
    where GENDER = 'MAN';

select ADDR, count(ORDER_NO) as 구매횟수
    from CUSTOMER_SALES_INNER_JOIN
    where GENDER = 'MAN'
    group by ADDR; 

-- 구매횟수 100회 미만 필터링
select ADDR, count(ORDER_NO) as 구매횟수
    from CUSTOMER_SALES_INNER_JOIN
    where GENDER = 'MAN'
    group by ADDR
    having count(ORDER_NO) < 100;