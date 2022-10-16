# Problem
# Amber’s conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy: 

# Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

# Note:

# The tables may contain duplicate records.
# The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.
# Input Format
# The following tables contain company data:

# Company: The company_code is the code of the company and founder is the founder of the company.
# Lead_Manager: The lead_manager_code is the code of the lead manager, and the company_code is the code of the working company.
# Senior_Manager: The senior_manager_code is the code of the senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company. 
# Manager: The manager_code is the code of the manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.
# Employee: The employee_code is the code of the employee, the manager_code is the code of its manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.
# Sample Input

# company_code	founder
# C1	Monika
# C2	Samantha
# Sample Output

# C1 Monika 1 2 1 2
# C2 Samantha 1 1 2 2
# Explanation
# In company C1, the only lead manager is LM1. There are two senior managers, SM1 and SM2, under LM1. There is one manager, M1, under senior manager SM1. There are two employees, E1 and E2, under manager M1.


# In company C2, the only lead manager is LM2. There is one senior manager, SM3, under LM2. There are two managers, M2 and M3, under senior manager SM3. There is one employee, E3, under manager M2, and another employee, E4, under manager, M3.

#------------------------------------------------------------

# Sorun
# Amber'in holding şirketi birkaç yeni şirket satın aldı. Şirketlerin her biri bu hiyerarşiyi takip eder:

# Aşağıdaki tablo şemalarına göre, şirket kodunu, kurucu adını, toplam lider yönetici sayısını, toplam üst düzey yönetici sayısını, toplam yönetici sayısını ve toplam çalışan sayısını yazdırmak için bir sorgu yazın. Çıktınızı şirket_kodunu artırarak sıralayın.

# Not:

# Tablolar mükerrer kayıtlar içerebilir.
# Company_code bir dizgedir, bu nedenle sıralama sayısal olmamalıdır. Örneğin, şirket_kodları C_1, C_2 ve C_10 ise, artan şirket_kodları C_1, C_10 ve C_2 olacaktır.
# Giriş Formatı
# Aşağıdaki tablolar şirket verilerini içerir:

# Şirket: Şirket_kodu şirketin kodudur ve kurucusu şirketin kurucusudur.
# Lead_Manager: Lead_manager_code, lider yöneticinin kodudur ve company_code, çalışan şirketin kodudur.
# Senior_Manager: Senior_manager_code, üst düzey yöneticinin kodudur, lead_manager_code, lider yöneticisinin kodudur ve company_code, çalışan şirketin kodudur.
# Yönetici: Yönetici_kodu, yöneticinin kodudur, üst düzey_yönetici_kodu, üst düzey yöneticisinin kodudur, lead_manager_code, lider yöneticisinin kodudur ve şirket_kodu, çalışan şirketin kodudur.
# Çalışan: Çalışan_kodu çalışanın kodudur, yönetici_kodu yöneticisinin kodudur, üst düzey_yönetici_kodu üst düzey yöneticisinin kodudur, lead_manager_code onun lider yöneticisinin kodudur ve şirket_kodu çalışanın kodudur. şirket.
# Örnek Giriş

# company_code kurucusu
# C1 Monika
# C2 Samantha
# Örnek Çıktı

# C1 Monika 1 2 1 2
# C2 Samantha 1 1 2 2
# Açıklama
# C1 şirketinde tek lider yönetici LM1'dir. LM1 altında SM1 ve SM2 olmak üzere iki üst düzey yönetici bulunmaktadır. Üst düzey yönetici SM1'in altında bir yönetici, M1, vardır. M1 yöneticisi altında E1 ve E2 olmak üzere iki çalışan vardır.


# C2 şirketinde tek lider yönetici LM2'dir. LM2 altında bir üst düzey yönetici olan SM3 vardır. Üst düzey yönetici SM3'ün altında M2 ve M3 olmak üzere iki yönetici vardır. M2 yöneticisinin altında bir çalışan, E3 ve M3 yöneticisinin altında E4, başka bir çalışan var.

select c.company_code, c.founder, count(distinct lm.lead_manager_code), count(distinct sm.senior_manager_code), count(distinct m.manager_code), count(distinct e.employee_code) from Company c, Lead_Manager lm, Senior_Manager sm, Manager m, Employee e
where c.company_code = lm.company_code and lm.lead_manager_code = sm.lead_manager_code and sm.senior_manager_code = m.senior_manager_code and m.manager_code = e.manager_code group by c.company_code, c.founder
order by c.company_code