-- https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes

/* 조건에 맞는 회원수 구하기 */

select count(USER_ID) from USER_INFO
    where (JOINED >= '2021-01-01' and JOINED <= '2021-12-31') 
    where JOINED between '2021-01-01' and '2021-12-31'
        and (AGE >= 20 and AGE <= 29)
        and AGE between 20 and 29;

/* 역순 정렬하기 */

select NAME, DATETIME from ANIMAL_INS
    order by ANIMAL_ID desc;

/* 여러 기준으로 정렬하기 */

select ANIMAL_ID, NAME, DATETIME from ANIMAL_INS
    order by NAME asc, DATETIME desc;

/* 기준으로 정렬하기 */


