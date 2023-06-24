-- https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes

/* 동물의 아이디와 이름 */

select ANIMAL_ID, NAME from ANIMAL_INS
ORDER BY ANIMAL_ID asc

/* 어린 동물 찾기 */

SELECT ANIMAL_ID, NAME from ANIMAL_INS 
where INTAKE_CONDITION != 'Aged'

/* 상위 n개 레코드 */

SELECT NAME FROM ANIMAL_INS
WHERE DATETIME = (SELECT min(DATETIME) FROM ANIMAL_INS)
-- SELECT min(DATETIME) FROM ANIMAL_INS

/* 아픈 동물 찾기 */

select ANIMAL_ID, NAME from ANIMAL_INS
where INTAKE_CONDITION = 'Sick'