SELECT ROUND(ABS((MIN(lat_n) - MAX(lat_n))) + ABS((MIN(long_w) - MAX(long_w))), 4)
FROM station;
--mysql & oracle
--here I learnt about the ABS() function