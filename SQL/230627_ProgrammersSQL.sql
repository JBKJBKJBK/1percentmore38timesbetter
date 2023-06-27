/* NULL 처리하기 */

select ANIMAL_TYPE, if(NAME is null, 'No name', NAME) as NAME, SEX_UPON_INTAKE
    from ANIMAL_INS
    order by ANIMAL_ID;

/* 경기도에 위치한 식품창고 목록 출력하기 */

select WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, ifnull(FREEZER_YN, 'N')
    from FOOD_WAREHOUSE
    where ADDRESS like '경기도%'
    order by WAREHOUSE_ID asc;