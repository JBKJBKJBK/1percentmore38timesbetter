SELECT A.*
    FROM places AS A
    -- WHERE B.등록수 > 1
    LEFT JOIN (SELECT HOST_ID
                        , COUNT(ID) AS 등록수
                 FROM places
                 GROUP BY HOST_ID
              ) AS B
    ON A.HOST_ID = B.HOST_ID
    WHERE B.등록수 > 1
    ORDER BY A.ID;
