/*
SELECT T.MEMBER_NAME
        , T.REVIEW_TEXT
        , T.REVIEW_DATE
        , T.작성수
        FROM  (SELECT A.MEMBER_ID
                    , A.MEMBER_NAME
                    , B.REVIEW_TEXT
                    , B.REVIEW_DATE
                    , COUNT(B.REVIEW_TEXT) AS 작성수
                FROM MEMBER_PROFILE AS A
                LEFT JOIN REST_REVIEW AS B
                ON A.MEMBER_ID = B.MEMBER_ID
                GROUP BY A.MEMBER_ID
               ) AS T
*/
CREATE TABLE JOINTABLE AS
SELECT A.MEMBER_ID
        , A.MEMBER_NAME
        , B.REVIEW_TEXT
        , B.REVIEW_DATE
        , COUNT(B.REVIEW_TEXT) AS 작성수
    FROM MEMBER_PROFILE AS A
    LEFT JOIN REST_REVIEW AS B
    ON A.MEMBER_ID = B.MEMBER_ID
    GROUP BY A.MEMBER_ID;
    
-- 확인
SELECT * FROM JOINTABLE;

SELECT MEMBER_NAME
        , REVIEW_TEXT
        , REVIEW_DATE
        , 작성수
        FROM  JOINTABLE

        /*
        WHERE T.작성수 = 3 이렇게 하면 실행됨
        WHERE T.작성수 = MAX(T.작성수) 로 하면 에러.
        "
        SQL 실행 중 오류가 발생하였습니다.
        Invalid use of group function
        "
        */
        WHERE T.작성수 = (SELECT MAX(A.작성수)
                            FROM (
                                    SELECT A.MEMBER_ID
                                        , A.MEMBER_NAME
                                        , B.REVIEW_TEXT
                                        , B.REVIEW_DATE
                                        , COUNT(B.REVIEW_TEXT) AS 작성수
                                    FROM MEMBER_PROFILE AS A
                                    LEFT JOIN REST_REVIEW AS B
                                    ON A.MEMBER_ID = B.MEMBER_ID
                                    GROUP BY A.MEMBER_ID
                            )AS A)  -- 실행됨
        -- ORDER BY

/* TEST
SELECT A.MEMBER_ID
        , A.MEMBER_NAME
        , B.REVIEW_TEXT
        , B.REVIEW_DATE
        , COUNT(B.REVIEW_TEXT) AS 작성수
    FROM MEMBER_PROFILE AS A
    LEFT JOIN REST_REVIEW AS B
    ON A.MEMBER_ID = B.MEMBER_ID
    GROUP BY A.MEMBER_ID;
*/

/* TEST 결과 : 3
SELECT MAX(A.작성수)
    FROM (
            SELECT A.MEMBER_ID
                , A.MEMBER_NAME
                , B.REVIEW_TEXT
                , B.REVIEW_DATE
                , COUNT(B.REVIEW_TEXT) AS 작성수
            FROM MEMBER_PROFILE AS A
            LEFT JOIN REST_REVIEW AS B
            ON A.MEMBER_ID = B.MEMBER_ID
            GROUP BY A.MEMBER_ID
    )AS A
*/  