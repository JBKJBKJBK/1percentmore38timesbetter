/*
    from        : 테이블 확인
    where       : 테이블에서 특정 조건
    group by    : 열 별로 그룹화 (ex. 거주지역별)
    having      : 그룹화된 새로운 테이블에서 특정 조건
    select      : 열 선택
    order by    : 열 정렬
*/

/*

*/

/* 1 */
use PRACTICE;

select * from CUSTOMER;

select * 
    from CUSTOMER
    where GENDER = 'MAN';

select ADDR, count(MEM_NO) as 회원수  /* count */
    from CUSTOMER
    where GENDER = 'MAN'
    group by ADDR;

select ADDR, count(MEM_NO) as 회원수  /* count */
    from CUSTOMER
    where GENDER = 'MAN'
    group by ADDR
    having count(MEN_NO) < 100;

select ADDR, count(MEN_NO) as 회원수
    from CUSTOMER
    where GENDER = 'MAN'
    group by ADDR
    having count(MEN_NO) < 100
    order by count(MEM_NO) desc  /* desc : 내림차순, asc : 오름차순 */