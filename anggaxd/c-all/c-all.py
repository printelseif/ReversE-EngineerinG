# Author : Angga Kurniawan
# GitHub : https://github.com/anggaxd
# News Update
import base64
exec(base64.b64decode('IyBPYmZ1c2NhdGVkIGJ5IFB5IENvbXBpbGUKIyBDcmVhdGVkIGJ5IEhUUi1URUNIIChodHRwczovL2dpdGh1Yi5jb20vaHRyLXRlY2gpCiMgSW5zdGFncmFtIDogQHRhaG1pZC5yYXlhdAoKaW1wb3J0IG1hcnNoYWwsemxpYixiYXNlNjQKZXhlYyhtYXJzaGFsLmxvYWRzKHpsaWIuZGVjb21wcmVzcyhiYXNlNjQuYjE2ZGVjb2RlKCI3ODlDNDU5QUM5OEUzNDMxNzY5REZGNkU0OTlFNUVDMjFCMkZCNEU2QjhCMTBEMzM0ODQ2OTBDMTc5MDg0RTNCNDlEREIwMjVCNDIwNDNERERFNzhFQjE3RjQxQkQ5QjcwNEM5MkU1NDY1MjUzMjYzRTA3MEVGMzlERkM5QUFCRkY5RjVDRjVGN0YwRTNGRkYwNTdFRkVFOEUwRTE3N0YwRkQ5QjVGN0ZGOEY1RUJGQ0JGRTdCRkY5NzU3RUYzMkZDRjdGRkJFQkZDRjZEN0VGN0ZGREZBQkIzRkZCRjVGQkRGRkNGQUJCM0ZGRkY1RkJERkZFRkFCQkJGRjhGNUJCREZGRUZBNUZCRkY5RTc2RjM4RUNDRjNGNzg2ODdGRjk2NzcwQkRCRkZEM0ZGMDE1RkZGOEJGRkZGREFGNUY1OTI2RUQ5ODMzMTc2MzgxREU5MzUyQzY1NkRGQjRGMkVGQzE4NzMwNTk5MzFENTVFQjFFNkE0NEYxMjEyNEU1RjhDQTQyRkExMzY3QzZDNTQ3OEU1RjdCNTQxNjA5RTkzMTg3RTRGNThEMkM5QkRCMUZDRkYzOTlCQzU2OEVGOUI3Nzg5RURGNzBCQzI1Q0VFMjVBM0M1NTlFNzlDRDdDNzA4NjUzRTYwNTczOEUzMUNGQ0JGMDREMjlERjVGQzY3MDU5Q0VCRjhGMTMzQTBDNUZFQUYwQkQzMkU3RDE3MDVFM0FFNzhDNzBGRTczMkEzRjE4NTM3ODgzNDg0NjMyNEIzMzUzNEEwMkUyRkMxQ0NBM0E4MkFCN0VDQjUwNUUwNjRCNkYwOTRGMjdEN0I1MkQzMUZBNEI5OENEQ0QyODdFNjEyQTM2MkZGNjVDMUYyMURFNzg0RDUwM0U0QkU4Q0JENzhGQjlDN0QyRkI5RDJGQ0RCM0M1RjIxRTdCQzg5QkY0QjkyNDZEODU3QjQ3RTY5RTMwMjA4NDM3N0VDQkQxQkEyQUJBRDhDNEUxNkVDMjZCRkQ5ODcxNkQ1RDY5NjI2RjFDMzMzRjA1M0ZBMzk0M0VEOTkxRjMyNUI3N0RERkFGMEFEMzY2MkRBOTI3RjVENDUwRjMyNEFBMkUyMTYxRDQ5RTg4NzRDQkJCREM0NTU5NTU5QUM5RENCQzFENDlGM0ExNDdDODZCRTNDNjJEMUFFODNDOTExOENGNEFCQ0NFMzgzMTg2NjIzRkM3MTFBMjU3QjE0RkY1RkRFNEFGOUY0MEI3NzhDODZBRDUxQTE2NTg4RDFENTlEMUQwQjM4Q0JEMUYxRDA1Nzk4RTc1MDhFQjI0Nzg3MjM3QTJGNkZFQjY5RTk4Qzg1OTAyNjZCQUY4QTYzNzNGRDIzODVCNDQ5NkIwRUNFMUFDQkJGQkU3Nzg5NUY1QkNCMjYyOTExQjNEMTg5RkY5NjUyRERDRkQ0OUZDNjkxN0Y2NkMzOUI4NkI4RkY0NDNGMzdFQ0I5NEZFRDI0ODA3NTJBQTlDMEZCRUE3RkM2NDIzQjlCNzJEMTJCOTRCN0ZGNUQyQjM5QkM4NUUzRTM3MENGRDNBQkI5QTgxNkEyRDE0QURFQjVFODJBNkI4M0VDRjhFOUY5NkExQTdDMTgwODY4RUQ5QzQ0REMyNjg4NEVEMTVFNTM1RDVGMkVGQjNBRTAxNDVFNkQxNTI4NTBDREM0NEJBNUUxODhBQ0JBNTEzN0Q1NTM1QUVFQzU4NzlBMkE5OENENEYyRjIyQUJFNkIxRUVDQzVCRUVFRTRDRUI4QjQwRDQ2MzRFRDlCNzhDNTdDQzgxRUVFNTA5QzZBMzgwQTFCNjRBMDEyRjE5QzlGQzE0NEE4Mjg2NUI4NDZGNENBQzhGQkU5RDc0QkNCNjIzNDczRDYzMDdCMTRDOThCQkE1Nzg2RTNBQzk3NDFCRTMyMzNFQUM5NDcwNjEzOUE5ODNDMzRCM0U4RkRBMkZFNUE1RkJCREU0MUMzNEFERTU3OTUyRjhBQjE1RUNBRDM1MDVCNjI5MTc1NjM5RDcwNUI1NTNBMkIzMTFENzVBOTNEN0EwMkQ0OTBFQTdFNDhCNEExRkVFMDREMjM3QjQxNzBCNEVENTA2MkI5Rjc0NDkxRkMxQzEyQzM5QjE3Q0ZFQUY0QjIzN0JFRTJDQUNBODg3MjcxQTYxMUFFMTI4NkMyOEM0Mzc3MkE4OUM5NjY5NTE5RTFFNkU5MDQ2MTYxODE3QTQ3RTFGQTUwNjAwRjBBMTREMUZDRDA0RTVCRTczNzYyOEJBRjZFNDVENEU1Q0QzMTcxNDE3MTQ2QUY2MjJFMTkyMkI2OEMzQUI1NjA5NTk0NTNBOUE3QURENzhGRUY4MTBEMTk1NzUxOTJCODcyNzc3QkE5QjlEMjVFRUNCQzc3MThCMDFDRUYxQkM2N0U2N0FDNDNENzdCNjM5MTcyM0I5MjUwN0FCRDNBOUExNzZBNDM0RTNENEJEOUUzMzU0MjM0MzE1QUU1RTg3MjUwMkQyRTM5MEI4RDlBOUVEMjZCNDVBMzI4REY5ODcyQ0RFQURBOEJDNkZCRjVBNUZBNTQ2MDE0REYzREVEN0E2Mjk4RTJBQkM2M0YxRTlBRUNBNUE2NjgyMkVFRUIzQzFEQjcwQ0I1MjNCNEVCMkE0NzExOEUyNkNERENFQUI1QTAwMTJGMDk5QjA2RTI2Njg2MjI4MDU1MjExQjdEMTk0QUU4OTk1NERENkU2QTREQUU0RUJFMzg4NjFBRjY0RUU4RjREMEJGMkI5Qzc0NDlGRkUyQUM1Mzk5RTM4Q0U3ODAzQTNFRDYyQTZENzI5Q0Y4Qjk0MDUwQUZCNEE0OEUzMDg4NkY2MUMzQkUyMkY5Nzg2OUY0NkY4OUVGRjAzRDQ0N0FFN0IwNzdCNTlFM0YxOEEzRTU1NDM2NTYxMUM0NTM5MDY3QUVBRjYwODdFRkRDQ0M2OEE5NDhCMUExOTgwQjM1NzRDOEM4MEZEQUNEQURGNTI5NkQ3NTE3Mjk1NTk0OEI2RTMyNTkxRDAzMjFGNEFCQTUzRTU2MzdENzI1QjlGMEIzMzdCQkE1QTdFMjk4NjM5MDBEMjcwRkE2REE5NzEzODc4NjkwNjE5RUM4NDJCMjI3MjAzQzk5NzlERUI1RjI1NTYxQkYyQjRGNTIwNzUxMEFDQzNBOUMyRkU0NUQ2RTQ1QTEyRTFEQzhGRjJERUU1QTc3QzI4MzBFOTQ1MUVBNDE1NTNGMUQ5NThBMzU5MDhFNzFFODkzMjgxNTlFMjE4MzMyQTY3OTNCMUE5N0JEMDJEOTBEMkE4NDNGNjYwNzJBNTc2MTNBRUY3N0NGQ0QwMzVGNjlDNDQ0NjA1MkI3NEVFRjIxMUM4QjExRDcyODI4M0JGQjk0OUQzRjI1OTI0ODE4RUVERDc3NjI4MjdDM0JENkZCNEFBQzgxQUU1NzJERjhFOUJCRDBEREM3NjhDMUJGQkU2NjcwQTY5MzExQUE0OUFGQzRFN0I3QUExMDhDRERDMkU3NDc5OERCNDA0RjdFMTMxNzI2MEM1NEVEMUQ1RkU0REY0MzlENUQxRjM3MDgzOTYyN0QxRUIxRTg2QkZBOEI0RUI2M0M2N0I1NUY2NDc4NTRDODNFREI1NzE3NjY2RjZGN0VDNjA1NjYyOTFCMEM5NzdEQ0VCMDg1Q0VFNjlCN0MzMkNBQjk4NEM4REQyQkE4QTZCNzJGQjAzNzFFNzQ2RTIyNjA2NEJCMTZFNjVBMDE0RkQxMTRDRkNDNjRDMkFBMERDQ0I0RUFEQzBBNzVDQUQ0N0Q3RERBOTRFQ0M2RjIzREU4NzFGNzdCOUU0MkEwRkQzQUEyQTVEQzMyMDg4NzczNERFRkQyOUM1ODE1OUQ5NTA2N0Y2NTExNTAyRjMzRERDQjJFOEY5OUNDRUE3OUMyQTMyNEIzMjZDOUM3NzlCRDNGMEExMzAyMDM5ODI4MjE2OEY3OEFDRDUzRTk3MzhDM0YzNzhFRTg3ODUwREVCQTFFMEM3NTczNkI0OUZEMzU0NzNGNzhFRkMzMDc5OEYyQjNCNkMyQkQzNjJCQTEzNDhFQkYwQUIyQTMyMUFERjM4NENFQjMzQkNGNkIyMjFFOUU5ODFCN0QzQTk1QThFODMzRUY3NEU0NzUzQ0IzQzE4MjVENzQwMzAyNDQ0MDZGRDg2MTRFMjhFNTFEMDg4MjQ0NkREQjI4OUY1NTBEMjNFQTJFMkZCQTEyQTlGQzI2MjAzQjEzRkM0Rjk5REM1RUI5NDk3Q0U2QUFFN0UzMDg0ODA0REUwQjk1N0E5Q0EyMjJGQzNBQjg5RjQyMEVDMjE0M0NDNjE5N0QwQzI1NzQ5RDUxNTY0Qzc5RjlCOUU4RkI3OTFERDI5MzY1MzZCMzM4RjIzM0IyNkUzRTYzREM0QkRCOEE2QzI1RjQyNDkxNzU3RkIxNDBDQ0YxQURFMjYzMDI0QjYzMjk3N0ExOUMwOEEyRTFCQjQzMTFGRDkzMkJBMDM1QTQ3NjA1RUZENEQ4NDc2RUE1ODdDOEY5NUE0NDM3MzU2RjY0RUEyNkMzNzZEOEM5RjRFNkQxMTY4REMyMDc2NEQ3Q0JCMzE5NzU3MDU5REZCMkJGMkQyOTVEMDA0MzBBQTYyOUQ0OUQ2OThCNTg4RjJGNDYwOTZGQ0EwMDFBRTJDQzM4QjJDQTI0QTM4OTVFN0ZBMEE0RkM2MzA4Q0UwNzdEMTIxODM3MDYxQUZEMjhGMDlENDc3RDA1OTQ1NDAyMTFFREU0MjUyMkMxNjNBOERBOEZDRDExRkE1RTI0NUFDNEYwMjIzNEM4OUI2RTQwQjYyNDE3NEE0MzFGNzFGNEZCRjAyOTFGRENBODNGRTk5RDE0RERENzAwMjQ3ODcxOUY2OTk3MkYzN0RGNDczOTU2OTI3MkQxRjdCODU5REJDMzU2RUM4MTc0NENFRDIwQTc3RTcyQ0Y4OTUxRDA2MTU2RkVGNDc3NjE2RUIxNzNCQ0JDMDU4RDlBQjFCRjA2Nzc4MUUyRDUzRkFCQUQ0RDIwMzdDM0M5NTIzRjYyNzg4OEM2NTAyREVBMjMxQkVBRTI4MkE3REI1RUM1NDRBOUY0Q0QzQUJFM0NCQzcxQUNCRjcyQzlDRkVEMzAxQkY4MTFDNzI5RTRCNTc1M0NDQUFBNUI4NDg1Q0EzOEUxQkIzRTRFRkU5ODI0NDVCOUVGQUYyRkREMTkwMjFDRjUzNkFBQ0NEQ0ZENjkyODg5MEZDRjkwNjdFRkNGMEQyQTBFNzA2MzM1MkJFMzZCNUU3NUQzNUM1OUYzMzQ1MDIwRTVENDRCQkZDMjgwMjRENkZFMTBBODhFMjg1MEUxQ0E4RTQ4NzU0MUMwQTExNjdGN0UwQURBNDI3OTNFMjkxNDdCM0ZCNUMxQkE4QURCMDAzMTdDQTY5MURGMjczQUE4OTY3MjBBMTczMDcwMkY2Q0E2RTc4RDc3Mzk4NjFEOEQ0OURGQTBFODBFNENFRTJCQjRFN0Q3OUY2NjRFRjk4MDkyRjQyOTEyOENERUZCQTAxRjdEMUYyMUQ0MTlEMjg4MkZCRkYyMEE1Q0MxQjcwQkU0NTk3Q0M0REQ5MDRDQkJDMzUwNUExQ0VGNzVBM0U4MkVEMTI5NzkxOTZCMzBGNzI3MkYzNzU4MzUwRjAxNkNDM0ZFQjVCNzg5MDFDQTQ4NDU0QkRFOUU0NDI3Qzg3RDQ2ODIyQ0Y0MDBGREU1QTQyMDkyMDRBNzlEMjk0QTE0RjE0RDdEMTMxNkM0MDFDNTYzNjMwMUUxMEUyODZFMTgzQjkxOTdCODQyMjRFNUJERTVGNkQyOURCREU2NDNERDgwNjE2M0E3Q0JBNERCMjhCQkM5Q0FGMkUzQUEyQjIxRkRCQ0RBRkRCQzc1N0I2QUJGNkUzNDZCNjQyQjY0OUM5MkFEQzE1ODhGQjdBRjdGNjFFQkEwNTQ4QzVBRTBGRjQ2MjE3MDQzNEJDNTY3NzE1MDIwMzQzNzEyNTczQzJFNUM2MjZFMEQ3ODMxNDQ2QjM1MUYyQ0QzMEJBRkM5NTZFQURFNjI2ODA1RDAwMEZENzQ1Njc0ODA2QjhEMzhBNjJGRjBFMTlDMjRFQzNCNzQ2RjE3RTJDMUJFOTY0RkRGMzAzOTAzMDE4NThCMDQwNDQ3MEI4MDA3NDBEOTYzNENGQTE4MkZBRUNBRUYwQ0QyQTNBNDhGOUREQ0ZBNjNEQzFDMTcxRkNDNzIzMzYwRjI4MkI4MkQ5MDQ1QTI2QjQwNTRCRUMxQzY3MjFDMDg1RjNGQjVBQjcwODUzRUQ0RTZDMjYyNkJFMzlCQzI0NzY2MTEwMTRGNjAwRDk2MDFFMjRCQTg0RERDNDA4QTZBOURDQjQ0NEQyRjkyOUVFN0Y1MkU5MzRCNkVCODA3ODk5NzYyOUQxOEY2REVFNkQzRDRGQkREOUZGMzg2MkVFQ0VCQkE3RUJFNEEzMkM0MUQ1NjAyMDA3QTM5NzI2MDBDQjYwMzJCQUZDQUFCODE3OEMwRUNGMjBFODNEODNFNTcwNjExNThBNDk0RkM5RTg0NUNCQUVGQjNCQTg0NjhFMjBBNzI4Rjk4QTBBQ0NDOUUxN0REQzVCRkVCODREMUUxREEwRDNDRTRDNTg4NjREMUI2MEZERUM1QzRGQUQ0QTdEREE2OTNFQUJFQjcyQUYzOTFCMDJFRUQ0MUNFNTc2MEYxNEFFOTJFMkNDRkVBRDk3QzNGQjQxOUY0RTlGMzA1N0M2MTAzQkIzRDc3QjZDRjlBNzIzQjA5MDY0OTY2NDkyMEU4QzlFNTY0NzAxRjNENkJBMzQyMDA1N0VCQzgxMzA2MkI4RTMwRTQ5Q0IxNjA4QjcyRUMzNzQwM0RFOEQ2RTBDNUFBNjdENEZEOEMwREU3Q0ZCNjU2OTBGMjdFMjExMDg4MTA2MTZENjkwMjJDMjJFQTg1MDVCRTAyMjU5N0E1RjE2NTZFODExNzBDMEU0OTgxMjVGM0FENjFDNDQxMENCODZGQjk3QjVFRTQ4MDdFNDUxNTYxQTNDMDEyNUZDREE5MjNFN0EyMDhFQzlDMjJGNEUwRkExREQ4MTlDRTA0NkFFNTI1QjI4MjUzMDRBNEIyMTdBNEQxQjFDNDFERUY1QkRGMzhEQkFBQUJFQjM2OTdGNkRFMTBBRjc2QTZFNEFFMUVBRjQ3M0QwODcwM0M0RDM3QzZEODMwOUFGRDQzNjg5MEFGRTc4N0NDNTEyRjIxRUI5MUU0RDMzOEIxMTQyNkM4QTgxMTk2Mjk0RTZFQTQwMjE4Q0E4N0FGRTZCRTUzMjY5NzVDODdBREI1NTlCOUYxOEY4ODBDOTUxMUVBNzgxQTU1RTQ4MzZDRkFGNDI5RDYyQ0Y0QjMyQ0IzNDMxNTlEMUQzQ0Y1NkUxMEE0MTgzMDVFNjc0MDE3NkU4NjM0QURGRTIwMkE3MUU3MjA2NjAzODM0Rjc5RUY5NzNGRDI5QkU1RTI3NTk3MkIxRDA0OTlEMDAxNzkyMUU2RUIwMUNFODI4QjkxRTg1QzBGQzM0NTkyQjc5NjlCQzNCNTEzOTQwM0E3QzFEQUU5NUNBQ0JDMDIxOEJFQUJFREZCODI3QTc4QzJGNTA0ODU5RERDMzA4REZCMTY5MTM0REJFREFBMzYwQTRFNDhEQTc2MDJDMEZBRUM2QTIzQkU5OEEwOEI4MENEMDdDRTUyMzU1QTdDNzc5MEZGNjI2ODEzQTA1MzlDMTUyREE1MURBQjE2NEU3QTY5RTNFQUFENjhCQTVDRTBEODRFMUZEMkY5MDY0NDIzNTZBRUVGNDVBRjg3MjA2QkUyMTMxRjhFQUI4NzdBNUQzOTNDOTBDMzY0ODE5MDk2QzU1MUNERThDRjI2ODJBRkVGNzYyMDg3OUYzN0U3RUIxQjI2ODJFQzRDNDZBRjJENDkxQjlEREQ4MUJFRUREQzhBMDgwNjVDN0JFNDBENzA3NTZBRTA2RjBERjdEN0YyOERGMkM1Mjk0MTM3NTdFRkQ3RTdBMzgwQTUyRDkxRDY0MDhFOTkyN0Q3Q0I3NUJGRDVENTk1NkQzRTkzMEUyMkIwNjEyNjVBRDNGOEUxRjdBNzI5MEFBOUVCQTQ0RkVCMDdBMjY0ODVCOUJFNjA1OEZFQTcwQTk0NDVFMEU0NDM5NjYwREEzMTNBN0M3OTg5RUIxOTgyODcwQjdGNEQwODAxQTFENUJFRjIzMDMxMjQ4NDU1MDk2MThENUM4ODNGQ0JGQjg3MjY1NTg2QzM1NTc5RTg1RDg4MzVERDIwNzk1RkI0MjcyOEQ1NDdGQjBCOEVCQkI4NzE4RjlDRjEyQUFDMEE3RkJCNUVFRDM2QzU4NjVEQzU2MDcwMjhEQjYwM0U0MEY1QUMwMDgzNThFODA2Mjg5NjIxMDQxNEIxQkE1RUQ5OTlDNTFEQ0Q3REE0QjYyODkzN0I2OTc3RTk0RjFBRUJDMUYyQTVCQUQzNTc3ODZDREYxQjAxNDI2QUJENUU5MDAzNUVCRUI5NkY5Rjc2OEREMTdEQkQ1NTk2RjcwNjlCMzg4RTk2RjAzOEM4OTMwNjBFM0NDOTVBNkZGQzI1NjdDRDkwRTkzODM4RDE3NDU5RDZFOTA1MjQ5QkE1QUZCNUY5ODUwRUM4RTFCQzIwM0JBOEQ5RUVENDBGQzFBMEQ1Nzg1MTI4MTgwNjM3MjQzMkJDMzc1QTlFRkE4Q0VCNTg5MzI1N0JGNzcwMUIwMEI2MTcyOUVGRTdCRTkyQkQyNkM2NzJDRTNEMDlCNDU4RjYzMTJCRTY0MTlDRjY5QkY0N0I2OTM3RjlFN0M0NTkzQjQ5QTQyMEM5M0IyNjJBQTQzMjU4RDBBRTU1M0FEQjg0NzA5RjAzQUY0MkZFNURGQTMxQ0ZFNTgxMzZEMDM3NTZGNjhGNTU0MEIxNzg2NTJEMUZDM0I2MzJFNkQ0RDc3MzhFNTA4RjlDNDNCMDU0REY2MTU5NEM2QjI5M0FDODQ2ODhFNDMzQjU3NUNBQzBFNzc2QjBFNzQ3NDc0MDg3RDFGOTZCQzAwM0I0NEJDM0NDQ0QwMDU0QzIzOUU0ODNGODBFMkEzODg3MDMwNEMzQTc3RjJGMjgyQkE1MDBENzVBQTA0NThDNDRCNENGNDgwODAxMjQ2RTc1QzhGNjE4RTFBNjlGRTFDMTVDREUzRUM2RUM3M0Q2MkYyQTVGNDM5NzI5NzdFRDlGMkE0RUFGQUJGQkM3MTFGQThBQjQ5NTg0ODJDNTM5NDNBQTFEM0M4MzQ3NTAwOTM4MzJFRTZDMEY3NDQ4NEUzOTEwN0VERURENDhGRjlFMEQ1RDI3NTg4NzNCMDRBMkE3MDBBOEVCMTA1QTZGN0Y3MThFMzM3NTBFRjkxQzczRTA1N0ZGRTYwQjFDMzlCMzU2M0EyMThGNUY0NjI0RDRDNEEwRTFCQzYwQzQzRTA5OUE5RDFDQzhGOTA4RDIwQTFENjhGOUY4OTgxNzY1MTA0RTFBRUNGNkRDNjAwNDJDQjdGOEYyRjg3RDM4RjM2NEVFMDNBNEY4N0VBM0EyMkVGOTk1NTMzQjMyMDE2MTA4MzRBQzIxNzlEQ0VFODIyNTFBRUY1NzM3MjRDQzc4NTFGRTU0MDRFQzhFOTcwM0VCQjBGREQxMTNDOUE5RDUxRDAxMDkzQUQ3RjEyRDcwREM4Q0YzRjMwRkFDNzU4MDdDMEZDODNDMkREMDVFN0U1N0QyNjA4NzE2RDY3Rjc3QkUyMDdGQUQwMEQ3OTM5MDEwRTM4NUYzMkRGMDlFQzI2RDM4QkQ1MUMzMjAwMURBMTlDMEQxMzk2MUY3MzQzMDkxRjMzQUEyQUI0MjVEMUJGRTQxMEMwNTdENkQxMzdBQjBFMTIyNTMyOEZERUNFMDA2RkQ0MDFCNUE3NjhFNDBCOTAwQUYyOTA4MDM0REZDQTg1NEMzQjdFN0M4RDIyMkVBMTU1OTI0QTBGNjc3N0JDNERERDg0NUE2ODM0Mjg2NjUzNkVBOTEzQzVBRjcwRDE1Q0Q0NjU3QjBFRDZCNzcyNEZFNTU0MzIyMDc2QjM4Mzg5ODlENTA4RDlGOTFDMzRBOUIzRUY4NjdBRjFDMDBDNzFCNUE4QzEwMDJBMTlGNjYwM0NFMEU0OUU1RjA4RTYwRjhGQkU5MDIzQzRFNjg0NDZFNDhBRjM2MDQ0ODQ4OTM1RkIxOTY1MUVFNjE0REIyMUVCMTRERTg3OEQ4QUYwODgxMUY2NDhFQzlGRERBQTg0NzUyQTc0OTA4NTdBMzFCNDIyRTgwMDY2MEExOUEzOTZEQjlFQ0FEOUIzMzlDNzNDNzA1M0EzODRFRDRGMjY1RkE4NUU5ODU5Rjc4RkNDRUU3NzE1NUMzRERDNkVDOUI1NDA0NjZFNjI4N0I3NjgzMjVCNjU3OEY0NUJDMTc3QUVDOTI2OEIwM0RDMENGRDhFNUUwOTY5MDUzMDBBNDIxREFBM0YxRTQ5QkU2OUY5MkJEQTQ4NkU3OUEyQjg5OEZCRkM5OURBNTAzMzI4N0FBNDQzNzcwN0M3REI1QzJEM0E2N0QwQkU2MjlEQzEyMkI4MDEzNkNFRTYyNjEzNDcyNjFGNTYzOTMxQjU3MERGQTA0MTZEOTRGQjBBMjJDMzEzRTJBNUJFODkxRkEyRTFFMzBGNzhGOUM0RkQ4MUQxRUEwQzc4QkNEQ0I5RTBGODFFMDgwQjI1NDQ4MzkxOTIxQzhENTk1NTEzMUIwRTk5OTY4QkY5NzA1MTQ2Qzc3ODYyRUJGNTc0QjI4RDlDQ0VGMzc2RkY5NTY2NzI5RTBDNjAzNDExOUY5RkJFNkI5Qjc5RUUwNjVDODU1QkMwNTExOTAxNENFRERGNjgzNTYxODcxMTE0NUE5QjRGQzQ2Nzc0RDc4NjIzN0FENEYyMDVBQTEzNTBDOEQ1Q0U3M0IxRkUwQzlFRTdEQTIwNDc4NkI2OTUyRTIyMzUxOEVBMjk4NTZDMUMyNkVGMzM0MDM5NEZDQjQwNDk5MTU2MkUwQzQ2M0VFQ0EyRkQwRkFDQTUzN0ZDOERENDEyRTc1RkYwQzY0Mzk4Mjk5OUZEMDNGRTFENkI0MDMxMTk5MDVGRTAxQjE1QUNERUQ1RDg1MzAwMTRDNjhDNTM4MTExRDU3MDBCOUExMzdFQTY5Mjk1RkEzRkM3Q0Y2QzZENUUyNTRERTkxNjI3MDkxNkIwMkE2RjQ1QzZFQzU2Rjg4MTVEQ0JGNjVFNkJCMzg1NkFGRkJCNjQwMkFDQ0EyMTBCMkRDMDVFODQxRjlDOTNFMzNFMzVFRTlGMUIwOTU2QjU2QTc5RUFCQzI3OTdBMTFFNEQ3NTIxRDkxNTdDMjgxMUE0MUFGNjhDQzVBMTgzQUFCQTc5RkRFRDFBOUVEQUFFRkNERERCQjkwREY0N0RDNkY4RjQ0MEVERTgwMkM1RjJCMjc2Rjk2NDIxMkUzRkVCOTgxQjYwNkMxMTBGNDA2OUY0QjQyMTRENTkwQjM4RjQ5OTEyNEIzMDNGOTJFRDMwMkUyRTNFMTY4QTFDNzFDRkVFMkY2RTlCM0FDRkFDODY3RTAzQzgwMzcyQzBBRUMwMjA0MTk1MjI3QjJGREM1NTM1RkMzRUY1OEYzODg3NkVEMTYyQ0ZBQjE4OTAxRkIwMzMxQTVFQTk5RDhDMjIzNEQ0MEY5OUM5MUI3RTU1Q0Y2NDkxQkZENzQzODg1RDgwOUQ3QkFEOTNBNjI5M0U2MzFEOUJCNUY1QjhBMkJCOTU3NDM4Njc4MzlERDFGRTQ0NEY0REFFRjgzN0E1M0FGQkU2MUQ0MUJBNzM3N0VEQzgxOTUxOTZGOTUwMkVEM0JCNjcwRkEwQzAyN0M0MjBFQTQ0MzIzNTNBOUVFNzI4QUE4Mzk3NThBNjE1QzgxQjhGQzJBNTg2MjkwQzQ4MzFFOTQ1RjUwNkIzMUJCN0UxQkI0NTlCQ0FBNUJEMTJCNDFFOTAwMTc1NjE4N0M1RUEzRjkzMDc5Q0VEOUEzODI1OEUwQzNGM0I1QjhGMTY3MDQxNzVFNjhDQkE3RTY0ODc0OUJGMTg2MTdENzRCRDhFOENCNUUzRUEyMEZFQ0ExRDZDMDhBNEE3QjA5RjE3NTZCNjJBN0VCRkVGOTIwNTY5NDcyQzUwQzZCMzY2NTk1NkMwMkVBNUYwOTFBMjQxQUQ5NzcwREFFNDg2QTJFODI0OUQzNENCQTM0NTU3MjUwNDgwRTREODdCRTBCRkEwQ0U4NDQ3QUJFOTQwNzJGMzAwMUU5NEEwODVCRjRENDU1MjE0RjZENTA3NTQ2Q0Q5MjMzMjdFRTExMDhGMDNDRTAyRjc3MTJENUE1RDhDQTdDQTIzMDBFQTI1Njg2RjUxOTVBMEI5MEUyNjREMjBEODJGNDE2Njg5MkJERjkxNkQ1MkI2ODNCNTg0MjA3NzhGQzBBNjg2Q0M1QzE4QTg5NTY3Q0FERTcxRDE2QkZFNjMxM0YyNjczNTU3QTgwNTM0RkRERTdBRUUzNzBDMDVFNUY5NzVCRDdCQkQ0OTNBMjg1RjYzRkZCNTQ5RjM1QUNFMTg1MjcwQjVBNjhCMTM4NEFGMjhBOTFDRTU3QTI2Rjg2Q0VEODc1N0I0OUVCQzJDMDA3OEQ4RkQ1NTQ5MkY2RjZDMEUxNUNFODY1MzgxMUYyNEI0NDA0MjgyQUFDMjAyNkU0RkUxNEFEMEZCQjk3MTdDRkI1RTE0NDU2QTlGODE5MkMyQjlCREQzQURCOEREMjQzQjkyQTYwRjYzMzMyNDhGRjAxMzA0NzZCNDRGNEYyRDdDQUNGMjVENTk2RkQ4MDM3Qjc2MzIxQzg4MEE1NkEwNEVERDk4MzA5RUREMkYyOEI2QTQwREU5NjY4MUZFQ0NBQzdFQjEzRDE4NTZDMDVFQzBBNzU4RDcxMTBEODlCMzg1QTBGNzU0MjlEMTA2RUVDQUIwQjY3QkRDQjAyQzhFMzc0RkZGOTNDNEYxRUNBNUVBMUEwRTM3MjcxQThFRTAwMkNBQjU2MDI3OENFOTIyRDFGNzQxODc0N0MxMDJGMzkzMDM3NjlDQjQyMTUwNjQwMzhDRTMzRjVEMTEzNjQ0QjUxNEFGNUI0MjE2MzQyQjJCRThFOUY0NzAzNDA1MEUwNjIwQjMzQkNCRTRCMkY0QzE3QkY2Q0VEREQ1RkE5ODk3NEQ3MzJFMzNBQjkxMEE3RDg3N0EwODhFRjMyRDAwQkM2QzVDMEQ0OTc4MTYwNzk5MTM4MDRCMDMyRUNERjA0RTEwNTFEMTY3MjQwRjRCOEU1MDcyMkE4MDEwNURGNjZFNjJENkE3MjNDODM4M0EyQzkwRkE4RTU3ODExMTFBMDkwOEIyQkM4NzJFM0QyNUM4MDZFMDk4MzA5REQzQjEzQTNCRTY5NzdBNDRBQjI3QzM3ODI5MzMxQ0FCRjI3REMwNTdBMEMzQkUwOUQ4NzQxREJFQjQ2NTcyQTBDREZCQUJENEU2N0EwNTMzRkZCMjc1NkI4MjUzQTcyMTU4REYzNDMyQ0I0RDg2OTE3OUQ0MzJDMEZCMDk4QTdDNjM0NDExNTM1ODAxODdDQjAwREREQTVEMDk3MjRFRkQ4RUE3NkE3NDhDMTZGRkM2NURBQzExRjJCOUFFMzgxRkMwOEU0ODQyMTYyRTQ3NUZGRkNGRDRCMDM2M0ZFNTA2OUIyQjA5QjM5MDEwNTQxQTQwM0NFNUM2MDFFMUM3QTI5NERBMjJGODE2MUZGNkExOEU0MTY4RjFCQUVBN0M2RTgzRTEzODNFNTlERjQ2QTEwODUwMTU2RTA2Q0EzRjk3QjkyNUNEMEM3MUY4NDU1NEUzODE4MDdGN0Y5NDQ1OTgwMkRCRDZBNDlGRTU0QUQ3QjQyQzVBMEM5RURGREE2OEI1RkYxMTk5NkJDNDg5NUU3MEQyOTY3NUM0QzQ1QTRCRDcyNTAyNTkwNEE5NzA1MUI0NjlCMEM3Q0RCMDlBNTJENjQ5MjdDMDMzRkIxNTEwMTVDMUQ2NDM3REQ0QzAxNTA4MDYxMDM5NkQwQ0RGM0M3Q0Q4MTNENEFEN0E2RUExRDk3NkMwNDlBMDk5NkYyQzRBNzNDOUZDMzI5QTM4NjU1RDBCODQ2MDU2RTQ5QkZGREYzQTkzMDM3NzgxMEIyNDk0MkMwRDQ4RjdEMjg2NkYzOUIxQ0FCOUZCRjJCMUI0MzM5MjdEODcwRTZBMjIyMzM0REUzM0YxQzMzMDZGNkZCMTk0MzVDOEJCMEE3ODczMjQ1QzMxOTEzODY2OTU3RDIyRUE4NDNDRTYyQTIyREI2MDdGMjY5MTQxRjREMzRFMzE3MkU2NjZEMkM5MDY0MjA2RURGNzAwQ0MyOEE3MDc2MTZFNTMxMkZFQzc4MDQ3NzUyOUM1M0FBRjhDMUM4NzE0NkZFRTk0RkUwMUM0RUM0M0VGM0VEQTVGOEE3NEZFMEZFRDM1RkZFQUI1RkJGN0VGREU5NUZDM0MzREZGRkQ1M0ZGRUYxQkZGREQ1MUZGRUY0RjM5RjA0RkZGMzBGN0ZGQkQ3N0ZGQTc5RTdBRkZGRUE4RkJGNjdFNDRGN0YwMTRGRkZGMDBGN0ZGNUJCM0ZGRUU5REZGREZDN0JDMUVGRkZFNjFGRkVGRUJGRkZFM0VGRkZGOEM3M0ZGRERCOUY2MzMwRkE3OUU1NzdCRkZGQ0I5RjdGNDRGOEZGMEY3RkZDRURDRkIxRkZGNTRGRkYwNjdFRkRDN0JGRkY4N0RGRkQ4RjNGRkNGRTNGRkZDNUJGQkNGRTFGN0VGMzdGMDE1MEYwMkU0NCIpKSkp'))