/* 
    비교 연산자
    =, <>, >, <, >=, <=
*/

/*
    논리 연산자
    AND, NOT, OR
*/

/*
    특수 연산자
    between A and B : 사잇값 (등호 포함))
    not between A and B : 사이값 아닌 것 (등호 미포함
    in (리스트)
*/

/*
    LIKE 비교문자열
    like 'D%' : D로 시작
    like '%N' : N로 끝
    like '%EO%' : EO를 포함
    not like '%EO%' : EO를 제외
*/

/*
    is null : null 이면 true
    is not null : 값이 있으면 true
*/

/*
    산술 연산자 : +, -, *, /
*/

/*
    집합 연산자
    union : 2개 이상 테이블의 중복된 행 제거 (중복 :모든 열의 값이 같을 때)
    union all : 2개 이상 테이블의 중복된 행 제거 없음
*/

create temporary table SALES_2019
select *
    from SALES
    where year(ORDER_DATE) = '2019';

/*
    테이블1
    union
    테이블2
*/
select *
    from SALES_2019
    union
    select *
        from SALES;

select *
    from SALES_2019
    union all
    select *
        from SALES;