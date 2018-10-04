/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT LISTAGG(L1,'&') WITHIN GROUP (ORDER BY L1) 
FROM (Select L1 FROM (SELECT LEVEL L1 FROM DUAL CONNECT BY LEVEL<=1000) WHERE L1 <> 1 MINUS SELECT L1 FROM (SELECT LEVEL L1 FROM DUAL CONNECT BY LEVEL<=1000) A , (SELECT LEVEL L2 FROM DUAL CONNECT BY LEVEL<=1000) B WHERE L2<=L1 AND MOD(L1,L2)=0 AND L1<>L2 AND L2<>1);

-- OR

select listagg(r,'&') within group (order by r) first_numbers
  from (Select Rownum r
          from dual
       connect by rownum <= 1000) n1
 where n1.r<=1000
   and n1.r>1
   and not exists (select null 
                     from (Select Rownum r
                             from dual
                             connect by rownum <= 1000) n2
                    where n1.r>=n2.r*2
                      and n2.r>1
                      and mod(n1.r,n2.r)=0);
                     
-- OR
WITH prime AS (select level n from dual connect by level <=1000), primelist as (select n from prime x where x.n>1 and not exists(select * from prime y where y.n>1 and x.n>y.n and mod(x.n,y.n)=0)) select listagg(n,'&') within group (order by n) from primelist

