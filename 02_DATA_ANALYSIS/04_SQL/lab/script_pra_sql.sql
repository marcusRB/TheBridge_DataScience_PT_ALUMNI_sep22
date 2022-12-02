-- 1.
/*
 * Proporcionar los nombres de los clientes que empiezan por AGR. Queremos obtener el número
de cliente, nombre y NIF. Los datos deben aparecer ordenados por número de cliente en orden
descendiente.
 * 
 */
SELECT 
	cust_no
	,cust_name
	,cust_cif
FROM erp.tb_customer
WHERE LEFT(cust_name, 3)='AGR'
-- WHERE cust_name LIKE 'AGR%'
ORDER BY cust_no DESC;

-- 2.
/*
 * Proporcionar las facturas de clientes con dirección en la ciudad de Granada. Queremos obtener
el número de cliente, nombre de cliente, dirección, ciudad y número de factura. La consulta debe
estar ordenada por número de cliente ascendientemente y número de factura descendentemente.
 * 
*/
SELECT 
	tc.cust_no
	,tc.cust_name
	,ts.site_address
	,ts.site_city
	,ti.invoice_no
FROM erp.tb_customer tc
,erp.tb_invoice ti
,erp.tb_site ts
WHERE UPPER(ts.site_city) = 'GRANADA'
AND tc.cust_no = ti.cust_no
AND ts.site_id = ti.site_id
ORDER BY tc.cust_no, ti.invoice_no DESC;

-- 3.

/*
 * Proporcionar la/s compañía/s con mayor número de facturas. Queremos obtener el código de
compañía, el nombre de la compañía y el número de facturas. En caso de haber más de una
compañía, los resultados deben aparecer ordenados por nombre de compañía.
 * 
 * 
 * 
 */

SELECT co_name, num_fac
FROM (
SELECT tc.co_code, tc.co_name, COUNT(1) AS num_fac
 	FROM erp.tb_company tc, erp.tb_invoice ti 
 	WHERE tc.co_code = ti.co_code
 	GROUP BY tc.co_code, tc.co_name
 	ORDER BY 3 DESC
) AS tabla_temp
WHERE num_fac = (
		SELECT MAX(t.num_fac)
			FROM  (SELECT tc.co_code, tc.co_name, COUNT(1) AS num_fac
					FROM tb_company tc,
						tb_invoice ti
			WHERE tc.co_code = ti.co_code
			GROUP BY tc.co_code, tc.co_name) as t
);


SELECT tc.co_code, tc.co_name, COUNT(1) AS num_fac
 	FROM erp.tb_company tc, erp.tb_invoice ti 
 	WHERE tc.co_code = ti.co_code
 	GROUP BY tc.co_code, tc.co_name
 	ORDER BY 3 DESC
 	LIMIT 1;

 
 
 -- d
 /*
  * 
  * 
  * 
  * Proporcionar la lista de facturas que contienen más de 18 líneas de factura. Queremos ver el
número de factura, el cliente, el nombre de la compañía y el número de líneas en total. La
información debe estar ordenada por número de líneas de forma descendente y compañía.
  */

SELECT  invoice_no,  cust_name, co_name, num_fac
FROM (
	SELECT invoice_no, tc.cust_name, tco.co_name, COUNT(1) AS num_fac
 	FROM 
 	erp.tb_company tco 
 	,erp.tb_invoice ti 
 	,erp.tb_lines tl
 	,erp.tb_customer tc
 	WHERE 
 		ti.invoice_id = tl.invoice_id
 	AND ti.co_code = tco.co_code
 	AND ti.cust_no = tc.cust_no
 	GROUP BY invoice_no, tc.cust_name, tco.co_name
) AS tabla_temp
WHERE num_fac > 18
ORDER BY num_fac DESC, co_name;
 
 
 
 