-- 이름에 el이 들어가는 동물 찾기
SELECT ANIMAL_ID, NAME
    FROM ANIMAL_INS
    WHERE ANIMAL_TYPE = 'Dog' 
        AND (NAME LIKE '%EL%' OR NAME LIKE 'EL%' OR NAME LIKE '%EL')
    ORDER BY NAME


-- 중성화한 동물 찾기
SELECT ANIMAL_ID, NAME,
        CASE 
        WHEN SEX_UPON_INTAKE LIKE 'Neutered%' THEN 'O'
        WHEN SEX_UPON_INTAKE LIKE 'Spayed%' THEN 'O'
        ELSE 'X' END AS 중성화
    FROM ANIMAL_INS 
    ORDER BY ANIMAL_ID;

SELECT ANIMAL_ID, NAME,
        IF (
            SEX_UPON_INTAKE LIKE 'Neutered%'
            OR SEX_UPON_INTAKE LIKE 'Spayed%'
            , 'O'
            , 'X')
    FROM ANIMAL_INS 
    ORDER BY ANIMAL_ID;