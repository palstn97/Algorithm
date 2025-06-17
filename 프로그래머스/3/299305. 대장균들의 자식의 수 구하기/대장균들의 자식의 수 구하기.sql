-- 코드를 작성해주세요
SELECT
    A.ID, COUNT(B.ID) AS CHILD_COUNT    # B.PARENT_ID도 가능하지만 식별자를 세는 것이 더 명확
FROM ECOLI_DATA A
LEFT JOIN ECOLI_DATA B  # INNER JOIN 사용시 부모 없는 친구들은 출력이 안됨
    ON A.ID = B.PARENT_ID   # A 개체를 부모로 갖는 B 자식들을 연결
GROUP BY A.ID
ORDER BY A.ID;