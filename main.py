from Algorithm import Vertical

m_s = float(input("enter percentage of min support >>> "))
m_c = float(input("enter percentage of min confides >>> "))

obj = Vertical(m_s, m_c)
obj.run_algor()