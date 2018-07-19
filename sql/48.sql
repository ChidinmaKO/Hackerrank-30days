SELECT N, IF(P IS NULL, 'Root', IF(B.N IN (SELECT P FROM BST), 'Inner', 'Leaf'))
FROM BST b
ORDER BY N;
--mysql

SELECT n, CASE WHEN P IS NULL THEN 'Root' WHEN n IN (SELECT p FROM bst) THEN 'Inner' ELSE 'Leaf' END AS Node
FROM bst b
ORDER BY n;
--mysql & oracle

SELECT n, CASE WHEN p IS NULL THEN 'Root' WHEN EXISTS (SELECT p FROM bst b WHERE a.n = b.p ) THEN 'Inner' ELSE 'Leaf' END AS node
FROM bst a
ORDER BY n;
--oracle