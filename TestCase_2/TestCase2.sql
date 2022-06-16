-- Qual foi a receita de cada tipo de pagamento no dia 15 de Marco de 2018? 
--R$586,81 do tipo de pagamento 1
--R$23,8 do tipo de pagamento	2

select SUM(total_amount),payment_type from dbo.testcase 
WHERE cast(dropoff_datetime as date) = '2018-03-15' 
GROUP BY payment_type; 

-- Considere que corridas de taxi validas tenham de 1 a 5 passageiros. Qual a quantidade de corridas feitas com cada numero de passageiros?
--716 corridas com 1 Passageiro
--151 corridas com 2 Passageiros
--32 corridas com 3 Passageiros
--25 corridas com 4 Passageiros
--50 corridas com 5 Passageiros

select COUNT(*) as taxi_runs, passenger_count as number_of_passangers from dbo.testcase 
where passenger_count between 1 and 5 
GROUP BY passenger_count
ORDER BY passenger_count;

-- Considerando apenas as corridas que houveram pedagios (tolls), qual a media do valor pago em pedagios por corrida? R$6,74 OK

select SUM(tolls_amount)/COUNT(*) from dbo.testcase 
where tolls_amount > 0;

-- Qual a hora que mais comecaram corridas? Hora 22

select COUNT(*) as number_of_runs, DATEPART(hh, pickup_datetime) as pickup_hour from dbo.testcase GROUP BY DATEPART(hh, pickup_datetime)
order by COUNT(*) DESC;
